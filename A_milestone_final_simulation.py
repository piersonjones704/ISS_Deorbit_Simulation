import math
import numpy as np
from constants import *
from Runge_Kutta_Integration_Interface import *
from Orbital_Decay_Acceleration_Function import *
from Final_Burn_Acceleration_Function import *
from Reentry_Acceleration_Function import *
from Rocket_Trajectory_Acceleration_Function import *
import matplotlib.pyplot as plt

def final_simulation(altitude, velocity, timestep, orbital_decay_time,final_burn_time):
    '''
    The main function simulate the three stages of the tractory of the ISS sation.
    The main functions take the initial inputs of starting altitude, starting velocity, timestep, length of orbital decay stage, and length of final burn stage.
    Returns a plot of the trajectory of the truss, and the distance travelled from breakup to splashdown.
    '''
    od_time = np.arange(0,orbital_decay_time,timestep)
    fb_time = np.arange(0,final_burn_time,timestep)
    rt_time = np.arange(0, 8*rocket_burn_time, timestep)
    reentry_max_steps = 100000
    separation_altitude = 100000       # in meters
    total_rows = len(od_time)+len(fb_time)+(reentry_max_steps)+len(rt_time)
    pos = np.zeros((total_rows,2))
    vel = np.zeros((total_rows,2))
    time = np.zeros(total_rows)
    pos[0] = [0.0,altitude+R_EARTH]
    vel[0] = [velocity,0.0]
    time[0] = 0.0
    

    # Orbital Decay Phase
    interval = 0
    for i in range(len(od_time)):
        posnext, velnext = Runge_Kutta(orbital_decay_accel,pos[interval],vel[interval],timestep)
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep


    # Final Burn Phase
    for i in range(len(fb_time)):
        posnext, velnext = Runge_Kutta(final_burn_accel,pos[interval],vel[interval],timestep)
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep


    # Reentry Phase
    separation_pos = None
    separation_vel = None
    impact_pos = None
    impact_vel = None
    status = 'orbiting or escaped orbit'
    for i in range(reentry_max_steps):
        current_pos = pos[interval]
        current_vel = vel[interval]
        posnext, velnext = Runge_Kutta(reentry_accel, pos[interval], vel[interval], timestep)
        current_altitude = math.hypot(pos[interval, 0], pos[interval, 1]) - R_EARTH
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
            status = 'hit ground'
            break
        interval += 1
        pos[interval] = posnext
        vel[interval] = velnext
        time[interval] = time[interval - 1] + timestep
    else:
        print("Impact did not occur during simulation runtime")
    pos = pos[:interval+1]
    vel = vel[:interval+1]
    time = time[:interval+1]
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
        print("Impact did not occur, so the horizontal distance cannot be calculated")
    else:
        separation_unit_vector = separation_pos / np.linalg.norm(separation_pos)
        impact_unit_vector = impact_pos / np.linalg.norm(impact_pos)
        dot_product = float(np.dot(separation_unit_vector, impact_unit_vector))
        cross_z_component = float(separation_unit_vector[0] * impact_unit_vector[1] - separation_unit_vector[1] * impact_unit_vector[0])
        central_angle_rad = math.atan2(abs(cross_z_component), dot_product)
        # Surface arc distance
        horizontal_distance_meters = R_EARTH * central_angle_rad
        print(f"Horizontal distance from 100 km separation to splashdown: {horizontal_distance_meters:.1f} meters")


    # Rocket Trajectory Phase
    ct4 = 0
    for ct4 in range(len(rt_time)):
        posnext, velnext  = Runge_Kutta(rocket_accel,pos[ct4], vel[ct4], timestep)
        pos[ct4+1] = posnext
        vel[ct4+1] = velnext
    axs, figs = plt.subplots(1, 1)
    axs.plot(posnext, velnext)
    plt.show()

if __name__ == '__main__':
    final_simulation(275000,7700,1,90,60)
