import math
import numpy as np
from constants import *
from Runge_Kutta_Integration_Interface import *
from Orbital_Decay_Acceleration_Function import *
from Final_Burn_Acceleration_Function import *

def final_simulation(altitude, velocity, timestep, orbital_decay_time,final_burn_time):
    od_time = np.arange(0,orbital_decay_time,timestep)
    fb_time = np.arange(0,final_burn_time,timestep)
    pos = np.zeros((len(od_time)+len(fb_time),2))
    vel = np.zeros((len(od_time)+len(fb_time),2))
    
    pos[0] = [0,altitude+R_EARTH]
    vel[0] = [velocity,0]

    ct1 = 0
    for ct1 in range(len(od_time)):
        posnext, velnext = Runge_Kutta(orbital_decay_accel,pos[ct1],vel[ct1],timestep)
        pos[ct1+1] = posnext
        vel[ct1+1] = velnext
    ct2 = 0
    for ct2 in range(len(fb_time))
        posnext, velnext = Runge_Kutta(final_burn_accel,pos[ct2],vel[ct2],timestep)
        pos[ct2+1] = posnext
        vel[ct2+1] = velnext