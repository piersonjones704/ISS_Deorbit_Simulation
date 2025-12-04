from A_milestone_final_simulation import *
from constants import * 

def do_test(altitude, velocity, timestep, orbital_decay_time, final_burn_time, expected_status):
    final_ISS_status = main(altitude, velocity, timestep, orbital_decay_time, final_burn_time, testing = True)
    if final_ISS_status == expected_status:
        print('Test Passed', expected_status)
    else: 
        print('Test Failed. Expected:', expected_status, "Got:", final_ISS_status)

if __name__ == '__main__':
    # Test cases:
    do_test(275000, 7700, 0.1, 90, 60, 'hit ground')
    # When initial x velocity is below the impact velocity (7700 m/s) with the impact altitude value
    do_test(275000, 7000, 0.1, 90, 60, 'hit ground')
    # When initial x velocity is above the impact velocity (7700 m/s) with the impact altitude value
    do_test(275000, 8200, 0.1, 90, 60, 'orbiting or escaped orbit')
    # When initial altitude is below the standard 275 km that causes impact with the impact x velocity
    do_test(230000, 7700, 0.1, 90, 60, 'hit ground')
    # When initial altitude is above the standard 275 km that causes impact with the impact x velocity
    do_test(300000, 7700, 0.1, 90, 60, 'orbiting or escaped orbit')
    # When initial altitude and initial x velocity are both above their initial impact values
    do_test(300000, 8200, 0.1, 90, 60, 'orbiting or escaped orbit')
    # When initial altitude and initial x velocity are both below their initial impact values
    do_test(230000, 7500, 0.1, 90, 60, 'hit ground')
    # When initial alitude is 0 (immediate impact)
    do_test(0, 7500, 0.1, 90, 60, 'hit ground')   
    # When utilizing a small simulation run time value for orbital decay to prevent the ISS from impacting the ground
    do_test(275000, 7700, 0.1, 30, 60, 'orbiting or escaped orbit')   
    # When utilizing a small simulation run time value for final burn to prevent the ISS from impacting the ground
    do_test(275000, 7700, 0.1, 90, 20, 'orbiting or escaped orbit')   
    # When utilizing a negative tstep value
    do_test(275000, 7700, -0.1, 90, 60, 'invalid tstep value')   
    # When utilizing zero tstep value
    do_test(275000, 7700, 0.0, 90, 60, 'invalid tstep value')   
    # When utilizing a very large tstep value to make the function immediately run past impact
    do_test(275000, 7700, 10000.0, 90, 60, 'hit ground')   
