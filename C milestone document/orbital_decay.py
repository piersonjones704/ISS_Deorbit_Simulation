from constants import *
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
        ax = (Fg/r) * x
        ay = (Fg/r) * y 

        vy += ay * dt
        vx += ax *dt
        x += vx * dt
        y += vy * dt

        t += dt
        if r <= R_EARTH: 
            break
    plot_position_earth(x_val,y_val)
    return x_val, y_val, vy_val, vx_val, t_val

def main():
    # TODO: write me
    #This is the given initial conditions and parameters
    ##orbital_decay(400,7670,90)

#Comprehensive tests that provide complete coverage, Path coverage, checks proper fails and successes
    #Cases that fail, changes in initial velocity
   ## orbital_decay(400,7000,90)
    ##orbital_decay(400,7070,90)
    ##orbital_decay(400,7500,90)
    ##orbital_decay(400,7520,90)


    #Cases that fail, changes in initial altitude
  ##  orbital_decay(0,7670,90)
   ## orbital_decay(100,7670,90)
   ## orbital_decay(200,7670,90)
   ## orbital_decay(250,7670,90)

    #Cases that fail, slight changes to altitude and velocity
   ## orbital_decay(275,7600,90)    
    ##orbital_decay(300,7620,90)
   ## orbital_decay(350,7580,90)

    #Cases that succeed, changes in altitude
   ## orbital_decay(450,7670,90)
   ## orbital_decay(500,7670,90)
   ## orbital_decay(1000,7620,90)

    #Cases that succeed, changes in velocity
##orbital_decay(400,7700,90)
## orbital_decay(400,8000,90)
## orbital_decay(400,8500,90)

    #Cases that succeed, slight changes to altitude and velocity
    orbital_decay(300,8000,90)
    orbital_decay(350,8300,90)
      ##Time has been changed here to allow full orbit to be seen   
    orbital_decay(200,9000,1000)





    

if __name__ == '__main__':
    main()