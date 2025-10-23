from constants import *
from plot import plot_position_earth


def orbital_decay(altitude, velocity, time):
    vx = velocity
    vy = 0
    x = 0
    y = altitude + R_EARTH
    r = altitude + R_EARTH
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
    plot_position_earth(x_val,y_val)

def main():
    # TODO: write me
    orbital_decay(400000,7670,100)
    

if __name__ == '__main__':
    main()