from reentry_C_ import unit_converter_initialaltitude, second_order_ex, main
from constants import R_EARTH

def do_test(y0, input_unit, vx0, vy0, tstep, expected_status, max_steps = 100000):
    x0 = 0.0
    status, y0 = unit_converter_initialaltitude(y0, input_unit)
    if y0 is None:
        if status == expected_status:
            print('Test Passed', expected_status)
        else: 
            print('Test Failed. Expected:', expected_status, "Got:", status)
        return
    ts, xs, ys, vxs, vys, status, = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    if status == expected_status:
        print('Test Passed', expected_status)
    else: 
        print('Test Failed. Expected:', expected_status, "Got:", status)

if __name__ == '__main__':
    # Test cases:
    do_test(130, 'km', 7800, 0, 0.1, 'hit ground')
    # When initial x velocity is below the steady orbit 7800 m/s velocity with the steady orbit altitude and y velocity
    do_test(130, 'km', 7000, 0, 0.1, 'hit ground')
    # When initial x velocity is above the steady orbit 7800 m/s velocity with the steady orbit altitude and y velocity
    do_test(130, 'km', 8200, 0, 0.1, 'orbiting or escaped orbit')
    # When initial altitude is below the standard 130 km that enables a steady orbit with the steady orbit x and y velocity
    do_test(100, 'km', 7800, 0, 0.1, 'hit ground')
    # When initial altitude is above the standard 130 km that enables a steady orbit with the steady orbit x and y velocity
    do_test(150, 'km', 7800, 0, 0.1, 'hit ground')
    # When initial altitude and initial x velocity are both above their steady orbit values with a steady orbit y velocity value
    do_test(150, 'km', 8000, 0, 0.1, 'orbiting or escaped orbit')
    # When initial altitude and initial x velocity are both below their steady orbit values with a steady orbit y velocity value
    do_test(100, 'km', 7500, 0, 0.1, 'hit ground')
    # When initial altitude and initial x velocity are both at their steady orbit values but with an initial y velocity towards Earth
    do_test(130, 'km', 7800, -30, 0.1, 'hit ground')
    # When initial altitude and initial x velocity are both above their steady orbit values and with a small initial y velocity towards Earth
    do_test(140, 'km', 8000, 10, 0.1, 'orbiting or escaped orbit')
    # When initial altitude and initial x velocity are both above their steady orbit values and with a large initial y velocity towards Earth
    do_test(140, 'km', 8000, 150, 0.1, 'orbiting or escaped orbit')
    # When initial altitude and initial x velocity are both below their steady orbit values and with a small initial y velocity towards Earth
    do_test(110, 'km', 7200, -10, 0.1, 'hit ground')
    # When initial altitude and initial x velocity are both below their steady orbit values and with a large initial y velocity towards Earth
    do_test(110, 'km', 7200, -150, 0.1, 'hit ground')
    # When initial altitude units are changed to centimeters with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(13000000, 'cm', 7800, 0, 0.1, 'hit ground')
    # When initial altitude units are changed to meters with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(130000, 'm', 7800, 0, 0.1, 'hit ground')
    # When initial altitude units are changed to feet with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(426509, 'ft', 7800, 0, 0.1, 'hit ground')
    # When initial altitude units are changed to miles with initial altitude and initial x and y velocity both at their steady orbit values
    do_test(80.7783, 'miles', 7800, 0, 0.1, 'hit ground')
    # When initial alitude is 0 (immediate impact)
    do_test(0, 'm', 0, 0, 0.1, 'hit ground')
    # When utilizing a small max_steps value to prevent the ISS from impacting the ground
    do_test(130, 'km', 7800, 0, 0.1, 'orbiting or escaped orbit', max_steps=1)
    # When utilizing zero max_steps to prevent the ISS from impacting the ground
    do_test(130, 'km', 7800, 0, 0.1, 'orbiting or escaped orbit', max_steps=0)
    # When utilizing a negative max_steps value to prevent the ISS from impacting the ground
    do_test(130, 'km', 7800, 0, 0.1, 'invalid max_steps value', max_steps=-3)
    # When utilizing a negative tstep value
    do_test(130, 'km', 7800, 0, -0.1, 'invalid tstep value', max_steps=1000)
    # When utilizing zero tstep value
    do_test(130, 'km', 7800, 0, 0.0, 'invalid tstep value', max_steps=1000)
    # When utilizing a very large tstep value to make the function immediately run past impact
    do_test(130, 'km', 7800, 0, 300, 'hit ground', max_steps=1000)
    # When utilizing invalid starting units
    do_test(1, 'lightyears', 0, 0, 0.1, 'unit converter error')
