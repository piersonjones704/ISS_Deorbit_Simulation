from constants import *
import numpy as np
import math
from plot import plot_position_earth


def orbital_decay(altitude, velocity, time):
    altitudem = altitude * 1000
    vx = velocity
    vy = 0
    x = 0
    y = altitudem + R_EARTH
    r = altitudem + R_EARTH
    timetotal = time * 60
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
        rho = RHO_LEO*np.exp(-(altitudec/7500))
        Fd = .5*rho*(vmag**2)*(C_D_ISS*AREA_ISS+C_D_TRUSS*AREA_TRUSS)
        if vmag <= 0:
            Fd = 0
        ax = (Fg/r) * x - (Fd/(vmag*(M_ISS+M_TRUSS+M_DV))) * vx
        ay = (Fg/r) * y - (Fd/(vmag*(M_ISS+M_TRUSS+M_DV))) * vy

        vy += ay * dt
        vx += ax *dt
        x += vx * dt
        y += vy * dt

        t += dt
        if r <= R_EARTH: 
            break
    varray = np.column_stack((vx_val,vy_val))
    posarray = np.column_stack((x_val,y_val))
    tarray = np.array(t_val)
    return varray, posarray, t_val

def main():
    # TODO: write me
    #This is the given initial conditions and parameters
    varray, posarray, t_val = orbital_decay(275,7700,90)
    plot_position_earth(posarray[:,0],posarray[:,1])
    print(posarray[-1,1]-R_EARTH)

    

if __name__ == '__main__':
    main()