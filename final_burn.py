from constants import *
from plot import plot_position_earth
import math

def final_burn(altitude, velocity, time_minutes):
    # Constants
    thrust = 3236
    Cd = 2.07
    A = 1000.0
    m = 480000.0
    g = 9.1
    rho = 3.8e-12

    # Initial conditions
    R = R_EARTH + altitude
    x = R
    y = 0.0
    vx = 0.0
    vy = velocity

    dt = 1.0
    total_time = time_minutes * 60
    interval = int(total_time / dt)

    x_list, y_list = [], []

    for i in range(interval):
        
        r = math.sqrt(x**2 + y**2)
        ux, uy = x / r, y / r

        
        g_x = -g * ux
        g_y = -g * uy

        # Velocity magnitude and direction
        v = math.sqrt(vx**2 + vy**2)
        if v == 0:
            vx_unit, vy_unit = 0, 0
        else:
            vx_unit, vy_unit = vx / v, vy / v

        # Drag and thrust 
        drag = -0.5 * rho * Cd * A * v**2
        drag_x = drag * vx_unit
        drag_y = drag * vy_unit
        thrust_x = -thrust * vx_unit
        thrust_y = -thrust * vy_unit

        # vertical and horizontal accelaration
        ax = g_x + (drag_x + thrust_x) / m
        ay = g_y + (drag_y + thrust_y) / m

        # motion
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        x_list.append(x)
        y_list.append(y)

    # Plot results
    plot_position_earth(x_list, y_list)
    return x_list, y_list

if __name__ == '__main__':
    final_burn(220000, 7770, 60)
    final_burn(100000, 6000, 70)
    final_burn(50000, 10000, 120)