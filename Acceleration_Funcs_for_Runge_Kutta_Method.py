import numpy as np
from c_ms.constants import *
import math


def orbital_decay_accel(pos,vel):
    x = pos[0]
    y = pos[1]
    vx = vel[0]
    vy = vel[1]

    r = math.sqrt(x**2+y**2)
    altitudec = r-R_EARTH

    vmag = math.sqrt(vx**2+vy**2)
    rho = RHO_0*np.exp(-(altitudec/7500))

    Fg = -(G*M_EARTH)/ r**2
    Fd = .5*rho*(vmag**2)*(C_D_ISS*AREA_ISS)
    if vmag <= 0:
            Fd = 0
    ax = (Fg/r) * x - (Fd/(vmag*(M_ISS+M_DV))) * vx
    ay = (Fg/r) * y - (Fd/(vmag*(M_ISS+M_DV))) * vy
    return np.array([ax,ay])