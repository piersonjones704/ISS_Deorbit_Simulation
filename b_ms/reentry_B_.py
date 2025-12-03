import math
from constants import *
from plot import plot_position_earth
import numpy as np
 
def second_order_ex(x0, y0, vx0, vy0, tstep, max_steps):
    '''Uses parameters outlined in the reentry function to calculate the reentry position that will occur throughout the simulation run time, returns an array of velocity, position, and time, for the simulation and its status''' 
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
    total_mass = M_ISS + M_DV
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
        # Set distance from Earth's center
        r = math.sqrt(x*x + y*y)
        # Set altitude based off of Earth's center
        altitude = r - R_EARTH
        # End the function when the mass hits the ground
        if altitude <= 0:
            status = 'hit ground'
            tarray = np.array(t_list)
            posarray = np.column_stack((x_list, y_list))
            varray = np.column_stack((vx_list, vy_list))
            return posarray, varray, tarray, status
        vmag = math.sqrt(vx**2 + vy**2)
        rho = RHO_0*np.exp(-altitude/H_0)
        if vmag < 1e-12:
            ax_drag = 0
            ay_drag = 0
        else:
            Fd = 0.5*rho*(vmag**2)*C_D_ISS*AREA_ISS
            ax_drag = -(Fd / (vmag * total_mass)) * vx
            ay_drag = -(Fd / (vmag * total_mass)) * vy
        # Update x for each step
        ax_gravity = -mu * x / (r**3)
        ay_gravity = -mu * y / (r**3)
        ax = ax_gravity + ax_drag
        ay = ay_gravity + ay_drag
        vx = vx + ax * tstep
        vy = vy + ay * tstep
        x = x + vx * tstep  
        y = y + vy * tstep 
        t += tstep
        t_list.append(t)
        x_list.append(x)
        y_list.append(y)
        vx_list.append(vx)
        vy_list.append(vy)
    
    status = 'orbiting or escaped orbit'
    tarray = np.array(t_list)
    posarray = np.column_stack((x_list, y_list))
    varray = np.column_stack((vx_list, vy_list))
    return posarray, varray, tarray, status

# call euler simulation function with initial y, end time, and time step
def reentry(pos2, velo2, tstep, max_steps):
    '''Takes final altitude, final velocity from orbital decay function, time intervals, and a max simulation duration, and calls the second_order_ex function to calculate the reentry position that will occur throughout the simulation run time
        returns the array of velocity, position, and time, for the simulation and whether or not the station hit the ground or remained in orbit, given the initial parameters'''
    # Parameters
    x0 = pos2[-1, 0]
    y0 = pos2[-1, 1] 
    vx0 = velo2[-1, 0]
    vy0 = velo2[-1, 1]    
    pos, velo, ts, status = second_order_ex(x0, y0, vx0, vy0, tstep, max_steps)
    if pos is None:
        return None, None, None, status 
    return pos, velo, ts, status
    