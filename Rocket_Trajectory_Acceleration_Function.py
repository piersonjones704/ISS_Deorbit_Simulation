from constants import *
from plot import plot_simple
import numpy as np

wet_mass = M_0_LV
dry_mass = M_0_LV/MASS_RATIO_LV
fuel_weight = wet_mass - dry_mass
rocket_burn_time = (fuel_weight)/M_DOT_E_LV

def thrust(t):
    if t <= rocket_burn_time*0.7629:
        return M_DOT_E_LV*I_SP_LV*g_0
    else:
        return 0
    
def air_density(h):
    return RHO_0*math.exp(-h/H_0)

def drag_force(v, h):
    return 1/2*air_density(h)*v*abs(v)*C_D_LV*AREA_LV

def m(t):
    mass = M_0_LV - M_DOT_E_LV*t
    if mass > dry_mass:
        return mass
    else:
        return dry_mass  
    
def grav_force(t, h):
    return (G*M_EARTH*m(t))/(R_EARTH + h)**2
    #return g_0*m(t)


def rocket_accel(h, v, t):
    '''Function that returns the acceleration of the launch vehicle rocket.
    Takes altitude, velocity magnitude, and time as scalars. Returns scalar acceleration.'''
    return (thrust(t) - drag_force(v, h) - grav_force(t, h))/m(t)


