import math
import numpy as np
from constants import *
import matplotlib.pyplot as plt
from Runge_Kutta_Integration_Interface import *
from Orbital_Decay_Acceleration_Function import *
from Final_Burn_Acceleration_Function import *
from Reentry_Acceleration_Function import *
from Rocket_Trajectory_Acceleration_Function import *
from A_ms_plotting import plot_final_simulation


def final_simulation(altitude, velocity, timestep, orbital_decay_time, final_burn_time, testing = False):
    '''
    The main function simulate the three stages of the tractory of the ISS sation.
    The main functions take the initial inputs of starting altitude, starting velocity, timestep, length of orbital decay stage, and length of final burn stage.
    Returns a plot of the trajectory of the truss, and the distance travelled from breakup to splashdown.
    '''
    if timestep <= 0:
        return 'invalid tstep value'
    od_time = np.arange(0,orbital_decay_time*60,timestep)
    fb_time = np.arange(0,final_burn_time*60,timestep)
    rt_time = np.arange(0, 8*rocket_burn_time, timestep)
    od_steps = int(orbital_decay_time*60/ timestep)
    fb_steps = int(final_burn_time*60 / timestep)
    reentry_max_steps = 100000

    separation_altitude = 100000       # in meters
    total_rows = len(od_time)+len(fb_time)+(reentry_max_steps)
    pos = np.zeros((total_rows,2))
    vel = np.zeros((total_rows,2))
    time = np.zeros(total_rows)

    pos[0] = [0.0,altitude+R_EARTH]
    vel[0] = [velocity,0.0]
    time[0] = 0.0
    interval = 0


    # Orbital Decay Phase
    if not testing:
        print('ISS Deorbit Stage 1: Orbital Decay')
    for i in range(od_steps - 1):
        posnext, velnext = Runge_Kutta(orbital_decay_accel,pos[interval],vel[interval],timestep)
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep
    if not testing:
        print(f"Orbital Decay Final Altitude: {np.abs(np.linalg.norm(pos[interval]) - R_EARTH)/1000:.2f} km")
    if (np.linalg.norm(pos[interval]) - R_EARTH)/1000 == 0:
        status1 = 'hit ground'
        return status1
    else:   
        status1 = 'orbiting or escaped orbit'
        

    # Final Burn Phase
    if not testing:
        print('ISS Deorbit Stage 2: Final Burn')
    for i in range(fb_steps - 1):
        posnext, velnext = Runge_Kutta(final_burn_accel,pos[interval],vel[interval],timestep)
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep
    if not testing:
        print(f"Final Burn Final Altitude: {np.abs(np.linalg.norm(pos[interval]) - R_EARTH)/1000:.2f} km")
    if (np.linalg.norm(pos[interval]) - R_EARTH)/1000 == 0:
        status2 = 'hit ground'
        return status2
    else:   
        status2 = 'orbiting or escaped orbit'


    # Reentry Phase
    if not testing:
        print('ISS Deorbit Stage 3: Reentry')
    separation_pos = None
    separation_vel = None
    impact_pos = None
    impact_vel = None
    status3 = 'orbiting or escaped orbit'
    for i in range(reentry_max_steps):
        current_pos = pos[interval]
        current_vel = vel[interval]
        current_altitude = math.hypot(pos[interval, 0], pos[interval, 1]) - R_EARTH
        posnext, velnext = Runge_Kutta(reentry_accel, pos[interval], vel[interval], timestep)
        next_altitude = math.hypot(posnext[0], posnext[1]) - R_EARTH
        # Determine accurate separation altitude
        if separation_pos is None and next_altitude <= separation_altitude:
            altitude_change = current_altitude - next_altitude
            # fraction of the timestep where altitude == 100 km to determine a more accurate time value for separation
            if abs(altitude_change) > 1e-12:
                fraction_to_separation = (current_altitude - separation_altitude) / altitude_change
                fraction_to_separation = max(0.0, min(1.0, fraction_to_separation))
            else:
                fraction_to_separation = 0.0
            # interpolated separation position
            separation_pos = (current_pos + fraction_to_separation * (posnext - current_pos))
            separation_vel = (current_vel + fraction_to_separation * (velnext - current_vel))
        # Determine accurate impact altitude (first time <= 0 km)
        if next_altitude <= 0.0:
            altitude_change = current_altitude - next_altitude
            # fraction of the timestep where altitude == 0 to determine a more accurate time value for impact
            if abs(altitude_change) > 1e-12:
                fraction_to_impact = current_altitude / altitude_change
                fraction_to_impact = max(0.0, min(1.0, fraction_to_impact))
            else:
                fraction_to_impact = 0.0
            # interpolate impact position on Earth surface
            impact_pos = (current_pos + fraction_to_impact * (posnext - current_pos))
            impact_vel = current_vel + fraction_to_impact * (velnext - current_vel)
            # replace last stored with interpolated impact
            pos[interval] = impact_pos
            vel[interval] = impact_vel
            time[interval] = time[interval - 1] + fraction_to_impact * timestep
            status3 = 'hit ground'
            break
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep
    else:
        if not testing:
            print("Impact did not occur during simulation runtime")
    pos = pos[:interval+1]
    vel = vel[:interval+1]
    time = time[:interval+1]
    if not testing:
        print(f"Final altitude: {np.abs(np.linalg.norm(pos[interval]) - R_EARTH)/1000:.2f} km")
        print(f"Total simulation time: {time[interval]:.1f} seconds ({time[interval]/60:.1f} minutes)")
    # If no separation occurred, go to starting point
    reentry_start_interval = len(od_time) + len(fb_time)
    if separation_pos is None:
        if reentry_start_interval < len(pos):
            separation_pos = pos[reentry_start_interval].copy()
            separation_vel = vel[reentry_start_interval].copy()
        else:
            separation_pos = pos[0].copy()
            separation_vel = vel[0].copy()
    # Determine horizontal distance traveled by the truss
    # Convert separation and impact positions into unit vectors
    if impact_pos is None:
        if not testing:
            print("Impact did not occur, so the horizontal distance cannot be calculated")
    else:
        separation_unit_vector = separation_pos / np.linalg.norm(separation_pos)
        impact_unit_vector = impact_pos / np.linalg.norm(impact_pos)
        dot_product = float(np.dot(separation_unit_vector, impact_unit_vector))
        cross_z_component = float(separation_unit_vector[0] * impact_unit_vector[1] - separation_unit_vector[1] * impact_unit_vector[0])
        central_angle_rad = math.atan2(abs(cross_z_component), dot_product)
        # Surface arc distance
        horizontal_distance_meters = R_EARTH * central_angle_rad
        if not testing:
            print(f"Horizontal distance from 100 km separation to splashdown: {horizontal_distance_meters:.1f} meters")


    # Rocket Trajectory Phase
    rocket_pos = np.zeros((len(rt_time)))
    rocket_vel = np.zeros((len(rt_time)))
    rocket_time = np.zeros(len(rt_time))
    # Initial conditions for rocket (ground launch, vertical)
    rocket_pos[0] = 0.0
    rocket_vel[0] = 0.0
    rocket_time[0] = 0.0
    has_launched = False
    for i in range(len(rt_time) - 1):
        posnext, velnext = Runge_Kutta(rocket_accel, rocket_pos[i], rocket_vel[i], timestep, rt_time[i])
        rocket_pos[i + 1] = posnext
        rocket_vel[i + 1] = velnext
        rocket_time[i + 1] = rocket_time[i] + timestep
        has_launched = True
        #Check if rocket hit ground
        if rocket_pos[i + 1] <= 0 and has_launched == True:
            rocket_pos = rocket_pos[:i]
            rocket_vel = rocket_vel[:i]
            rocket_time = rocket_time[:i]
            break 
    max_altitude = (np.max(rocket_pos))/ 1000
    final_altitude = (np.linalg.norm(rocket_pos[-1])) / 1000
    if not testing:
        print(f"Rocket maximum altitude: {max_altitude:.2f} km")
        print(f"Rocket final altitude: {final_altitude:.2f} km")

    # Plotting
    if not testing:
        plot_final_simulation(pos, time, od_steps, fb_steps, separation_pos, impact_pos, rocket_pos, rocket_time)
        plt.show()
    return status3
    
def main(altitude, velocity, timestep, orbital_decay_time, final_burn_time, testing = False):
    '''The function that calls the final_simulation file and uses its output to print the final status of the ISS. Returns the final status of the ISS as well.'''
    # Status of ISS
    final_ISS_status = final_simulation(altitude, velocity, timestep, orbital_decay_time, final_burn_time, testing = testing)
    if not testing:
        print(f"Final ISS Status: {final_ISS_status}")
    return final_ISS_status

if __name__ == '__main__':
    main(275000,7700,0.1,90,60)
