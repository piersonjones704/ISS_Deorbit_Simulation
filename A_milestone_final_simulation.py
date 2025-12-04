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
    pos = np.zeros((len(od_time)+len(fb_time)+(reentry_max_steps),2))
    vel = np.zeros((len(od_time)+len(fb_time)+(reentry_max_steps),2))
    rocpos = np.zeros(len(rt_time))
    rocvel = np.zeros(len(rt_time))
    
    pos[0] = [0,altitude+R_EARTH]
    vel[0] = [velocity,0]

    ct1 = 0
    for ct1 in range(1,len(od_time)):
        posnext, velnext = Runge_Kutta(orbital_decay_accel,pos[ct1-1],vel[ct1-1],timestep)
        pos[ct1] = posnext
        vel[ct1] = velnext
    ct2 = 0
    for ct2 in range(1,len(fb_time)):
        posnext, velnext = Runge_Kutta(final_burn_accel,pos[ct2-1],vel[ct2-2],timestep)
        pos[ct2] = posnext
        vel[ct2] = velnext
    ct3 = 0
    for ct3 in range(1,reentry_max_steps):
        posnext, velnext = Runge_Kutta(reentry_accel,pos[ct3-1],vel[ct3-1],timestep)
        pos[ct3] = posnext
        vel[ct3] = velnext
    ct4 = 0
    for ct4 in range(1,len(rt_time)):
        posnext, velnext  = Runge_Kutta(rocket_accel,rocpos[ct4-1], rocvel[ct4-1], timestep, rt_time[ct4-1])
        rocpos[ct4] = posnext
        rocvel[ct4] = velnext
    axs, figs = plt.subplots(1, 1)
    axs.plot(posnext, velnext)
    plt.show()

if __name__ == '__main__':
    final_simulation(275000,7700,1,90,60)