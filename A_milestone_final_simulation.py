import math
import numpy as np
from b_ms.constants import *
from Runge_Kutta_Integration_Interface import *
from Acceleration_Funcs_for_Runge_Kutta_Method import *

def final_simulation(altitude, velocity, timestep, orbital_decay_time,final_burn_time):
    od_time = np.arange(0,orbital_decay_time,timestep)
    fb_time = np.arange(0,final_burn_time,timestep)
    pos = np.zeros((len(od_time)+len(fb_time),2))
    vel = np.zeros((len(od_time)+len(fb_time),2))
    
    pos[0] = [0,altitude+R_EARTH]
    vel[0] = [velocity,0]

    ct = 0
    for ct in range(len(od_time)):
        posnext, velnext = Runge_Kutta(orbital_decay_accel,pos[ct],vel[ct],timestep)
        pos[ct+1] = posnext
        vel[ct+1] = velnext