import math
from constants import R_EARTH, G, M_EARTH
from reentry import initial_altitude, input_units, x_initial_velocity, y_initial_velocity


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


if __name__ == '__main__': 
    # Import unit conversions for test cases of different initial units
    from ReentryUnits import unit_converter_initialaltitude
    y0 = unit_converter_initialaltitude(initial_altitude, input_units, output_unit = 'm')
    x0 = 0.0 
    time = 0
    tstep = 0.1
    max_steps = 100000
    vx0 = x_initial_velocity
    vy0 = y_initial_velocity
    mu = G * M_EARTH
    ts, xs, ys, vxs, vys, status = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)