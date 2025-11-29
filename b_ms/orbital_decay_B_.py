from constants import *
import numpy as np
import math
from plot import plot_position_earth

# Convert all input units for the initial altitude into meters.

def unit_converter_initialaltitude(starting_altitude, input_units):
    '''Alerts user if the unit conversion process has succeeded or failed'''
    y0 = initial_altitude_conversion_process(starting_altitude, input_units)
    if y0 == None:
        status = 'unit converter error'
        return status, y0
    else:
        status = 'unit conversion complete'
        return status, y0 

def initial_altitude_conversion_process(starting_altitude, input_units):
    '''Converts the units of the initial altitude from whatever is given into units that are easy to calculate with'''
    y = starting_altitude
    if input_units == 'km':
        y = y * 10**3
    elif input_units == 'm':
        y = y
    elif input_units == 'miles':
        y = y * 1609.344
    elif input_units == 'ft':
        y = y * 0.3048
    elif input_units == 'cm':
        y = y * 10**(-2)
    else:
        return None
    return y

def orbital_decay(y0, starting_velo, sim_time):
    '''Takes initial altitude, starting velocity, and length of simualtion, and calcualtes the orbital decay that will occur throughout the simulation run time
        returns the array of velocity, position, and time, for the simulation and whether or not the station hit the ground or remained in orbit, given the initial parameters'''
    # altitudem = starting_altitude * 1000
    altitudem = y0
    vx = starting_velo
    vy = 0
    x = 0
    y = altitudem + R_EARTH
    r = altitudem + R_EARTH
    timetotal = sim_time * 60
    dt = .1
    t = 0

    x_val = []
    y_val = []
    vy_val = []
    vx_val = []
    t_val = []
    while t <= timetotal:
        x_val.append(x)
        y_val.append(y)
        vy_val.append(vy)
        vx_val.append(vx)
        t_val.append(t)

        r = math.sqrt(x**2+y**2)

        Fg = -G*M_EARTH / r**2

        altitudec = r-R_EARTH
        vmag = math.sqrt(vx**2+vy**2)
        rho = RHO_0*np.exp(-(altitudec/7500))
        Fd = .5*rho*(vmag**2)*(C_D_ISS*AREA_ISS)
        if vmag <= 0:
            Fd = 0
        ax = (Fg/r) * x - (Fd/(vmag*(M_ISS+M_DV))) * vx
        ay = (Fg/r) * y - (Fd/(vmag*(M_ISS+M_DV))) * vy

        vy += ay * dt
        vx += ax *dt
        x += vx * dt
        y += vy * dt

        t += dt
        if r <= R_EARTH: 
            status = 'hit ground'
            varray = np.column_stack((vx_val,vy_val))
            posarray = np.column_stack((x_val,y_val))
            tarray = np.array(t_val)
            return varray, posarray, tarray, status
    varray = np.column_stack((vx_val,vy_val))
    posarray = np.column_stack((x_val,y_val))
    tarray = np.array(t_val)
    status = 'orbiting or escaped orbit'
    return varray, posarray, tarray, status

def orbital_decay_main(starting_altitude, input_units, starting_velo, sim_time):
    '''Connects all portions of the orbital decay process: unit conversion, unit conversion confirmation, and the orbital decay simulation
    Returns arrays for position, velocity, and time, and returns the status of the staion (If it hit the ground or remained in orbit)'''
    # Unit conversion function:
    status, y0 = unit_converter_initialaltitude(starting_altitude, input_units)
    if y0 == None:
        return None, None, None, status
    #This is the given initial conditions and parameters
    varray, posarray, tarray, status = orbital_decay(y0, starting_velo, sim_time)
    # plot_position_earth(posarray[:,0],posarray[:,1])
    # print(posarray[-1,1]-R_EARTH)
    return posarray, varray, tarray, status
    

if __name__ == '__main__':
    orbital_decay_main(275, 'km', 7700, 90)