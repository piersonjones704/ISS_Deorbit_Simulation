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
    return plot, status

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
