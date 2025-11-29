import numpy as np
import math
from c_ms.constants import *

def Runge_Kutta(accel,pos,vel,ts):
    k1 = accel(pos,vel)
    l1 = vel

    k2 = accel(pos + (ts/2)*l1,vel + (ts/2)*k1)
    l2 = vel + (ts/2)*k1

    k3 = accel(pos + (ts/2)*l2, vel + (ts/2)*k2)
    l3 = vel + (ts/2)*k2

    k4 = accel(pos + ts*l3, vel + ts*k3)
    l4 = vel + ts*k3

    veln = vel + (ts/6)*(k1 + 2*k2 + 2*k3 + k4)
    posn = pos + (ts/6)*(l1 + 2*l2 + 2*l3 + l4)

    return posn, veln