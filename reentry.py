from constants import *
from plot import plot_position_earth
from Eulersmethod_reentry import second_order_ex

    
# call euler simulation function with initial y, end time, and time step
def main(x0, y0, vx0, vy0, tstep):
    ts, xs, ys, vxs, vys = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    print(ts, xs, ys, vxs, vys)
    plot = plot_position_earth(xs, ys)
    return plot

if __name__ == '__main__':
    # Import unit conversions for test cases of different initial units
    from ReentryUnits import unit_converter_initialaltitude
    y0 = unit_converter_initialaltitude()
    x0 = 0.0 
    time = 0
    tstep = 0.1
    max_steps = 100000
    x_initial_velocity = 7800
    vx0 = x_initial_velocity
    y_initial_velocity = 0
    vy0 = y_initial_velocity
    mu = G * M_EARTH
    main(x0, y0, vx0, vy0, tstep)
    ts, xs, ys, vxs, vys = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    plot_position_earth(xs, ys)