import numpy as np
from constants import *
import math

def reentry_accel(pos, vel):
    x = pos[0]
    y = pos[1] 
    vx = vel[0]
    vy = vel[1] 
    mu = G * M_EARTH
    r = math.sqrt(x*x + y*y)
    # altitude in meters
    altitude = r - R_EARTH
    if r < 1e-12:
        ax_gravity = 0
        ay_gravity = 0
    else:
        ax_gravity = -mu * x /(r**3)
        ay_gravity = -mu * y /(r**3)
    if altitude <= 0:
        return np.array([0.0, 0.0])
    if altitude <= 100000: 
        mass = M_TRUSS
        cd = C_D_TRUSS
        area = AREA_TRUSS
    else:
        mass = M_ISS + M_DV
        cd = C_D_ISS
        area = AREA_ISS
    vmag = math.sqrt(vx**2+vy**2)
    rho = RHO_0*np.exp(-(altitude/H_0))
    if vmag < 1e-12:
        ax_drag = 0
        ay_drag = 0
    else:
        Fd = .5*rho*(vmag**2)*(cd * area)
        ax_drag = -(Fd / (vmag * mass)) * vx
        ay_drag = -(Fd / (vmag * mass)) * vy
    ax = ax_gravity + ax_drag
    ay = ay_gravity + ay_drag

    return np.array([ax,ay])
