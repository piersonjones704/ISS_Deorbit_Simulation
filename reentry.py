import math
from constants import *
from plot import plot_position_earth

# Parameters
initial_altitude = 130
input_units = 'km'
x_initial_velocity = 7800
y_initial_velocity = 0

def unit_converter_initialaltitude(initial_altitude, input_units, output_unit = 'm'):
    unit_conversion = initial_altitude_conversion_process(initial_altitude, input_units, output_unit)
    y0 = unit_conversion
    return(y0) 
    

def initial_altitude_conversion_process(initial_altitude, input_unit, output_unit):
    y = initial_altitude
    if input_unit == 'km' and output_unit == 'm':
        y = y * 10**3
    elif input_unit == 'm' and output_unit == 'm':
        y = y
    elif input_unit == 'miles' and output_unit == 'm':
        y = y * 1609.344
    elif input_unit == 'ft' and output_unit == 'm':
        y = y * 0.3048
    elif input_unit == 'cm' and output_unit == 'm':
        y = y * 10**(-2)
    return y

def second_order_ex(x0, y0, vx0, vy0, tstep, max_steps):
    # Set variables
    t = 0.0
    x = x0
    y = R_EARTH + y0 # Set y as the vertical distance from the center of Earth to the ISS
    vx = vx0
    vy = vy0
    # Set time, x, y, vx, amd vy list
    t_list = [t]
    x_list = [x]
    y_list = [y]
    vx_list = [vx]
    vy_list = [vy]
    # Calculate gravitational constant
    mu = G * M_EARTH
    for i in range(max_steps):
        # Set distance from Earth's center
        r = math.sqrt(x*x + y*y)
        # Set altitude based off of Earth's center
        altitude = r - R_EARTH
        # End the function when the mass hits the ground
        if altitude <= 0:
            status = 'hit_ground'
            return t_list, x_list, y_list, vx_list, vy_list, status
        # Update x for each step
        else:
            ax = -mu * x / r**3
            ay = -mu * y / r**3
            vx = vx + ax * (tstep)
            vy = vy + ay * (tstep)
            x = x + vx * (tstep)
            y = y + vy * (tstep)
            t += tstep
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)
        status = 'orbiting or escaped orbit'
    return t_list, x_list, y_list, vx_list, vy_list, status


# call euler simulation function with initial y, end time, and time step
def main(x0, y0, vx0, vy0, tstep):
    y0 = unit_converter_initialaltitude(initial_altitude, input_units, output_unit)
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
    y0 = 0
    xs = 0
    ys = 0
    output_unit = 'm' 
    # Unit conversion function for cases with different initial units
    initial_altitude_conversion_process(initial_altitude, input_units, output_unit)
    unit_converter_initialaltitude(initial_altitude, input_units, output_unit)
    second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    main(x0, y0, vx0, vy0, tstep)
    plot_position_earth(xs, ys)
