import math
import numpy as np
from constants import *
from Runge_Kutta_Integration_Interface import *
from Orbital_Decay_Acceleration_Function import *
from Final_Burn_Acceleration_Function import *
from Reentry_Acceleration_Function import *
from Rocket_Trajectory_Acceleration_Function import *
import matplotlib.pyplot as plt

def final_simulation(altitude, velocity, timestep, orbital_decay_time,final_burn_time):
    '''
    The main function simulates the four stages of the deorbit path of the ISS.
    The main function take the initial inputs of starting altitude, starting velocity, timestep, length of orbital decay stage, and length of final burn stage.
    Returns a plot of the trajectory of the truss, and the distance travelled from breakup to splashdown.
    '''
    od_time = np.arange(0,orbital_decay_time,timestep)
    fb_time = np.arange(0,final_burn_time,timestep)
    rt_time = np.arange(0, 8*rocket_burn_time, timestep)
    reentry_max_steps = 100000
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
    for ct2 in range(len(fb_time)):
        posnext, velnext = Runge_Kutta(final_burn_accel,pos[ct2],vel[ct2],timestep)
        pos[ct2+1] = posnext
        vel[ct2+1] = velnext
    ct3 = 0
    for ct3 in range(reentry_max_steps):
        pos, vel = Runge_Kutta(reentry_accel,pos[ct3],vel[ct3],timestep)
    ct4 = 0
    for ct4 in range(rt_time):
        posnext, velnext  = Runge_Kutta(rocket_accel,pos[ct4], vel[ct4], timestep)
        pos[ct4+1] = posnext
        vel[ct4+1] = velnext
    axs, figs = plt.subplots(1, 1)
    axs.plot(posnext, velnext)
    plt.show()

    