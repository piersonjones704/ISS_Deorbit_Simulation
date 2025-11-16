import math
from constants import *
from plot import plot_position_earth
import numpy as np
 
# Convert all input units for the initial altitude into meters.
# def unit_converter_initialaltitude(initial_x_position, input_x_unit, initial_y_position, input_y_unit):
#     x0, y0 = initial_altitude_conversion_process(initial_x_position, input_x_unit, initial_y_position, input_y_unit)
#     if y0 == None or x0 == None:
#         status = 'unit converter error'
#         return status, x0, y0
#     else:
#         status = 'unit conversion complete'
#         return status, x0, y0 

# def initial_altitude_conversion_process(initial_x_position, input_x_unit, initial_y_position, input_y_unit):
#     x = initial_x_position
#     if input_x_unit == 'km':
#         x = x * 10**3
#     elif input_x_unit == 'm':
#         x = x
#     elif input_x_unit == 'miles':
#         x = x * 1609.344
#     elif input_x_unit == 'ft':
#         x = x * 0.3048
#     elif input_x_unit == 'cm':
#         x = x * 10**(-2)
#     y = initial_y_position
#     if input_y_unit == 'km':
#         y = y * 10**3
#     elif input_y_unit == 'm':
#         y = y
#     elif input_y_unit == 'miles':
#         y = y * 1609.344
#     elif input_y_unit == 'ft':
#         y = y * 0.3048
#     elif input_y_unit == 'cm':
#         y = y * 10**(-2)
#     else:
#         return None, None
#     return x, y

def second_order_ex(x0, y0, vx0, vy0, tstep, max_steps):
    if tstep <= 0 and max_steps < 0: 
        status = 'invalid tstep and max_steps values'
        return None, None, None, status
    elif max_steps < 0:
        status = 'invalid max_steps value'
        return None, None, None, status
    elif max_steps == 0:
        status = 'orbiting or escaped orbit'     
        return None, None, None, status
    elif tstep <= 0:  
        status = 'invalid tstep value'
        return None, None, None, status
    # Set variables
    t = 0.0
    x = x0
    y = y0 
    vx = vx0
    vy = vy0
    total_mass = M_ISS + M_TRUSS + M_DV
    # Set time, x, y, vx, amd vy list
    t_list = [t] 
    x_list = [x]
    y_list = [y]
    vx_list = [vx]
    vy_list = [vy]
    # Calculate gravitational constant
    mu = G * M_EARTH
    status = ''
    for i in range(max_steps):
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)
        # Set distance from Earth's center
        r = math.sqrt(x*x + y*y)
        # Set altitude based off of Earth's center
        altitude = r - R_EARTH
        vmag = math.sqrt(vx**2+vy**2)
        rho = RHO_LEO*np.exp(-(altitude/7500))
        Fd = .5*rho*(vmag**2)*(C_D_ISS*AREA_ISS+C_D_TRUSS*AREA_TRUSS)
        # End the function when the mass hits the ground
        if altitude <= 0:
            status = 'hit ground'
            tarray = np.array(t_list)
            posarray = np.column_stack((x_list, y_list))
            varray = np.column_stack((vx_list, vy_list))
            return tarray, posarray, varray, status
        # Update x for each step
        else:
            ax_gravity = -mu * x /(r**3)
            ay_gravity = -mu * y /(r**3)
            ax_drag = -(Fd / (vmag * total_mass)) * vx
            ay_drag = -(Fd / (vmag * total_mass)) * vy
            ax = ax_gravity + ax_drag
            ay = ay_gravity + ay_drag
            vx = vx + ax * (tstep)
            vy = vy + ay * (tstep)
            x = x + vx * (tstep)
            y = y + vy * (tstep)
            t += tstep
        status = 'orbiting or escaped orbit'
    tarray = np.array(t_list)
    posarray = np.column_stack((x_list, y_list))
    varray = np.column_stack((vx_list, vy_list))
    return tarray, posarray, varray, status

# call euler simulation function with initial y, end time, and time step
def reentry(pos2, velo2, tstep = 0.1, max_steps = 100000):
    # Parameters
    initial_x_position = pos2[-1, 0] 
    # input_x_unit = 'm'
    initial_y_position = pos2[-1, 1] 
    # input_y_unit = 'm'
    x0 = initial_x_position
    y0 = initial_y_position
    x_initial_velocity = velo2[-1, 0] 
    y_initial_velocity = velo2[-1, 1]
    vx0 = x_initial_velocity
    vy0 = y_initial_velocity
    # Unit conversion function for cases with different initial units
    # status, x0, y0 = unit_converter_initialaltitude(initial_x_position, input_x_unit, initial_y_position, input_y_unit)
    # if y0 == None or x0 == None:
    #     return None, None, None, status
    pos, velo, ts, status = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    if pos is None:
        return None, None, None, status
    return pos, velo, ts, status
    # plot = plot_position_earth(pos[:,0],pos[:,1])
    # return plot, status

    