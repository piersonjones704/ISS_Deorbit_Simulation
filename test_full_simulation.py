from full_simulation_file import *
from orbital_decay_B_ import unit_converter_initialaltitude
from constants import * 

# Parameters
wet_mass = M_0_LV
dry_mass = M_0_LV/MASS_RATIO_LV
burn_time = (wet_mass - dry_mass)/M_DOT_E_LV

def do_test(starting_altitude, input_units, starting_velo, orbital_decay_sim_time, initial_rocket_launch_altitude, initial_rocket_launch_velo, rocket_launch_sim_time, tstep, reentry_max_steps, expected_status):
    x0 = 0.0
    status, y0 = unit_converter_initialaltitude(starting_altitude, input_units)
    if y0 is None:
        if status == expected_status:
            print('Test Passed', expected_status)
        else: 
            print('Test Failed. Expected:', expected_status, "Got:", status)
        return
    final_ISS_status = main(starting_altitude, input_units, starting_velo, orbital_decay_sim_time, initial_rocket_launch_altitude, initial_rocket_launch_velo, rocket_launch_sim_time, tstep, reentry_max_steps, testing=True)
    if final_ISS_status == expected_status:
        print('Test Passed', expected_status)
    else: 
        print('Test Failed. Expected:', expected_status, "Got:", final_ISS_status)

if __name__ == '__main__':
    # Test cases:
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')
    # When initial x velocity is below the steady orbit 7800 m/s velocity with the steady orbit altitude
    do_test(275, 'km', 7000, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')
    # When initial x velocity is above the steady orbit 7800 m/s velocity with the steady orbit altitude
    do_test(275, 'km', 8200, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'orbiting or escaped orbit')
    # # When initial altitude is below the standard 130 km that enables a steady orbit with the steady orbit x velocity
    do_test(230, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')
    # do_test(100, 'km', 7800, 0, 0.1, 'hit ground')
    # # When initial altitude is above the standard 130 km that enables a steady orbit with the steady orbit x velocity
    do_test(300, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')
    # do_test(150, 'km', 7800, 0, 0.1, 'hit ground')
    # # When initial altitude and initial x velocity are both above their steady orbit values
    do_test(300, 'km', 8200, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'orbiting or escaped orbit')    
    # do_test(150, 'km', 8000, 0, 0.1, 'orbiting or escaped orbit')
    # # When initial altitude and initial x velocity are both below their steady orbit values
    do_test(230, 'km', 7500, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(100, 'km', 7500, 0, 0.1, 'hit ground')
    
    # THIS SECTION TESTS FUNCTIONS FOR HAVING AN INITIAL Y VELOCITY (CURRENTLY NOT INTEGRATED INTO CODE)
    # # When initial altitude and initial x velocity are both at their steady orbit values but with an initial y velocity towards Earth   
    # do_test(130, 'km', 7800, -30, 0.1, 'hit ground')
    # # When initial altitude and initial x velocity are both above their steady orbit values and with a small initial y velocity towards Earth
    # do_test(140, 'km', 8000, 10, 0.1, 'orbiting or escaped orbit')
    # # When initial altitude and initial x velocity are both above their steady orbit values and with a large initial y velocity towards Earth
    # do_test(140, 'km', 8000, 150, 0.1, 'orbiting or escaped orbit')
    # # When initial altitude and initial x velocity are both below their steady orbit values and with a small initial y velocity towards Earth
    # do_test(110, 'km', 7200, -10, 0.1, 'hit ground')
    # # When initial altitude and initial x velocity are both below their steady orbit values and with a large initial y velocity towards Earth
    # do_test(110, 'km', 7200, -150, 0.1, 'hit ground')

    # # When initial altitude units are changed to centimeters with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(27500000, 'cm', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(13000000, 'cm', 7800, 0, 0.1, 'hit ground')
    # # When initial altitude units are changed to meters with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(275000, 'm', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(130000, 'm', 7800, 0, 0.1, 'hit ground')
    # # When initial altitude units are changed to feet with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(902231, 'ft', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(426509, 'ft', 7800, 0, 0.1, 'hit ground')
    # # When initial altitude units are changed to miles with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(170.8770834576, 'miles', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(80.7783, 'miles', 7800, 0, 0.1, 'hit ground')
    # # When initial alitude is 0 (immediate impact)
    do_test(0, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 100000, 'hit ground')    
    # do_test(0, 'm', 0, 0, 0.1, 'hit ground')
    # # When utilizing a small max_steps value to prevent the ISS from impacting the ground
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 1, 'orbiting or escaped orbit')    
    # do_test(130, 'km', 7800, 0, 0.1, 'orbiting or escaped orbit', max_steps=1)
    # # When utilizing zero max_steps to prevent the ISS from impacting the ground
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, 0, 'orbiting or escaped orbit')    
    # do_test(130, 'km', 7800, 0, 0.1, 'orbiting or escaped orbit', max_steps=0)
    # # When utilizing a negative max_steps value to prevent the ISS from impacting the ground
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 0.1, -3, 'invalid max_steps value')
    # do_test(130, 'km', 7800, 0, 0.1, 'invalid max_steps value', max_steps=-3)
    # # When utilizing a negative tstep value
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, -0.1, 1000, 'invalid tstep value')
    # do_test(130, 'km', 7800, 0, -0.1, 'invalid tstep value', max_steps=1000)
    # # When utilizing zero tstep value
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 0, 100000, 'invalid tstep value')
    # do_test(130, 'km', 7800, 0, 0.0, 'invalid tstep value', max_steps=1000)
    # # When utilizing a very large tstep value to make the function immediately run past impact
    do_test(275, 'km', 7700, 90, 0, 0, 8 * burn_time, 1000, 100000, 'hit ground')
    # do_test(130, 'km', 7800, 0, 300, 'hit ground', max_steps=1000)
    # # When utilizing invalid starting units
    do_test(1, 'lightyears', 7700, 90, 0, 0, 8 * burn_time, 0.1, 0, 'unit converter error')
    # do_test(1, 'lightyears', 0, 0, 0.1, 'unit converter error')
