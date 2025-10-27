from constants import *
from plot import plot_position_earth

# Parameters
initial_altitude = 130
input_units = 'km'
x_initial_velocity = 7800
y_initial_velocity = 0
    
# call euler simulation function with initial y, end time, and time step
def main(x0, y0, vx0, vy0, tstep):
    ts, xs, ys, vxs, vys, status = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    print(ts, xs, ys, vxs, vys)
    plot = plot_position_earth(xs, ys)
    return plot

if __name__ == '__main__':
    vx0 = x_initial_velocity
    vy0 = y_initial_velocity
    time = 0
    tstep = 0.1
    max_steps = 100000
    mu = G * M_EARTH
    x0 = 0.0 
    from ReentryUnits import unit_converter_initialaltitude
    # Import unit conversions for test cases of different initial units
    y0 = unit_converter_initialaltitude(initial_altitude, input_units, output_unit = 'm')
    from Eulersmethod_reentry import second_order_ex
    main(x0, y0, vx0, vy0, tstep)
    ts, xs, ys, vxs, vys, status = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    plot_position_earth(xs, ys)

def do_test(x0, y0, vx0, vy0, expected_status, max_steps = 100000):
    ts, xs, ys, vxs, vys, status, = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps=max_steps)
    if status == expected_status:
        print('Test Passed', expected_status)
    else: 
        print('Test Failed. Expected:', expected_status, "Got:", status)

# Test cases:
do_test(130, 'km', 7800, 0, 'orbiting or escaped orbit')
# When initial x velocity is below the steady orbit 7800 m/s velocity with the steady orbit altitude and y velocity
do_test(130, 'km', 7000, 0, 'hit_ground')
# When initial x velocity is above the steady orbit 7800 m/s velocity with the steady orbit altitude and y velocity
do_test(130, 'km', 8200, 0, 'orbiting or escaped orbit')
# When initial altitude is below the standard 130 km that enables a steady orbit with the steady orbit x and y velocity
do_test(100, 'km', 7800, 0, 'hit_ground')
# When initial altitude is above the standard 130 km that enables a steady orbit with the steady orbit x and y velocity
do_test(150, 'km', 7800, 0, 'orbiting or escaped orbit')
# When initial altitude and initial x velocity are both above their steady orbit values with a steady orbit y velocity value
do_test(150, 'km', 8000, 0, 'orbiting or escaped orbit')
# When initial altitude and initial x velocity are both below their steady orbit values with a steady orbit y velocity value
do_test(100, 'km', 7500, 0, 'hit_ground')
# When initial altitude and initial x velocity are both at their steady orbit values but with an initial y velocity towards Earth
do_test(130, 'km', 7800, -30, 'orbiting or escaped orbit')
# When initial altitude and initial x velocity are both above their steady orbit values and with a small initial y velocity towards Earth
do_test(140, 'km', 8000, -10, 'orbiting or escaped orbit')
# When initial altitude and initial x velocity are both above their steady orbit values and with a large initial y velocity towards Earth
do_test(140, 'km', 8000, -150, 'orbiting or escaped orbit')
# When initial altitude and initial x velocity are both below their steady orbit values and with a small initial y velocity towards Earth
do_test(110, 'km', 7200, -10, 'hit_ground')
# When initial altitude and initial x velocity are both below their steady orbit values and with a large initial y velocity towards Earth
do_test(110, 'km', 7200, -150, 'hit_ground')
# When initial altitude units are changed to centimeters with initial altitude and initial x and y velocity both at their steady orbit values
do_test(13000000, 'cm', 7800, 0, 'orbiting or escaped orbit')
# When initial altitude units are changed to meters with initial altitude and initial x and y velocity both at their steady orbit values
do_test(130000, 'm', 7800, 0, 'orbiting or escaped orbit')
# When initial altitude units are changed to feet with initial altitude and initial x and y velocity both at their steady orbit values
do_test(426509, 'ft', 7800, 0, 'orbiting or escaped orbit')
# When initial altitude units are changed to miles with initial altitude and initial x and y velocity both at their steady orbit values
do_test(80.7783, 'miles', 7800, 0, 'orbiting or escaped orbit')

