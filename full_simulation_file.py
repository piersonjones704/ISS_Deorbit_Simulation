from constants import *
from plot import plot_simple, plot_position_earth
import numpy as np
import matplotlib.pyplot as plt
from orbital_decay_B_ import orbital_decay_main
from final_burn_B_ import final_burn
from reentry_B_ import reentry
from rocket_B import *

def main(starting_altitude, input_units, starting_velo, sim_time, initial_launch_rocket_altitude, initial_launch_rocket_velo, rocket_launch_sim_time):
    
    # Stage 1: Orbital Decay
    print('ISS Deorbit Stage 1: Orbital Decay')
    pos1, velo1, ts1, status1 = orbital_decay_main(starting_altitude, input_units, starting_velo, orbital_decay_sim_time)
    if pos1 is None or velo1 is None or ts1 is None:
        return status1
    elif status1 == 'hit ground':
        return status1
    final_altitude_1 = np.abs((pos1[-1,1]) - R_EARTH) / 1000
    final_velocity_1 = np.linalg.norm(velo1[-1])
    print(f"Final altitude: {final_altitude_1:.2f} km")
    print(f"Final velocity: {final_velocity_1:.2f} m/s\n")
    
    # Stage 2: Final Burn
    print('ISS Deorbit Stage 2: Final Burn')
    pos2, velo2, ts2, status2 = final_burn(pos1, velo1, 60)
    if status2 == 'hit ground':
        return status2
    final_altitude_2 = np.abs(np.linalg.norm(pos2[-1]) - R_EARTH) / 1000
    final_velocity_2 = np.linalg.norm(velo2[-1])
    print(f"Final altitude: {final_altitude_2:.2f} km")
    print(f"Final velocity: {final_velocity_2:.2f} m/s\n")

    # Stage 3: Re-entry
    print('ISS Deorbit Stage 3: Reentry')
    pos3, velo3, ts3, status3 = reentry(pos2, velo2, tstep = 0.1, max_steps = 100000)
    if pos3 is None or velo3 is None or ts3 is None:
        return status3
    elif status3 == 'hit ground':
        return status3
    final_altitude_3 = np.abs(np.linalg.norm(pos3[-1]) - R_EARTH) / 1000
    final_velocity_3 = np.linalg.norm(velo3[-1])
    print(f"Final altitude: {final_altitude_3:.2f} km")
    print(f"Final velocity: {final_velocity_3:.2f} m/s\n")

    # Stage 4: Launch Vehicle Rocket
    print('ISS Deorbit Stage 4: Launch Vehicle Rocket')
    pos4, velo4, ts4 = approx(rocket_launch_sim_time, t_step = 0.1, initial_rocket_launch_altitude, initial_rocket_launch_velo)
    final_altitude_4 = (np.linalg.norm(pos4[-1]) - R_EARTH) / 1000
    final_velocity_4 = np.linalg.norm(velo4[-1])
    print(f"Final altitude: {final_altitude_4:.2f} km")
    print(f"Final velocity: {final_velocity_4:.2f} m/s\n")
    
    # Plotting
    x_positions = np.concatenate([pos1[:, 0], pos2[:, 0], pos3[:, 0]])
    y_positions = np.concatenate([pos1[:, 1], pos2[:, 1], pos3[:, 1]])
    # plot_position_earth(x_positions, y_positions)
    # plot_simple(ts4, pos4)

    """Plots Earth circumference and x-, y-position"""
    th = np.linspace(0, 2*np.pi,100)
    xearth = R_EARTH*np.cos(th)
    yearth = R_EARTH*np.sin(th)
    plt.plot(xearth, yearth)
    plt.plot((pos1[:, 0][0]), (pos1[:, 1][0]), 'go', pos1[:,0], pos1[:, 1], 'g-', (pos1[:, 0][-1]), (pos1[:, 1][-1]), 'g^')
    plt.plot((pos2[:, 0][0]), (pos2[:, 1][0]), 'ro', pos2[:,0], pos2[:, 1], 'r-', (pos2[:, 0][-1]), (pos2[:, 1][-1]), 'r^')
    plt.plot((pos3[:, 0][0]), (pos3[:, 1][0]), 'ko', pos3[:,0], pos3[:, 1], 'k-', (pos3[:, 0][-1]), (pos3[:, 1][-1]), 'k^')
    plt.axis('equal')
    plt.show()


    # # Status of ISS
    # final_ISS_status = status3
    # print(final_ISS_status)
    # return final_ISS_status

if __name__ == '__main__':
    reentry_tstep = None
    starting_altitude = 275
    input_units = 'km'
    starting_velo = 7700
    orbital_decay_sim_time = 90
    initial_launch_rocket_altitude = 0
    initial_rocket_launch_velo = 0
    wet_mass = M_0_LV
    dry_mass = M_0_LV/MASS_RATIO_LV
    burn_time = (wet_mass - dry_mass)/M_DOT_E_LV
    rocket_launch_sim_time = 8 * burn_time
    main(starting_altitude, input_units, starting_velo, orbital_decay_sim_time, initial_launch_rocket_altitude, initial_rocket_launch_velo, rocket_launch_sim_time)