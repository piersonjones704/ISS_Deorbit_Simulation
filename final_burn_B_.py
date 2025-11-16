from constants import *
from plot import plot_position_earth
import math
import numpy as np

def final_burn(altitude, velocity, time_minutes):
    # Constants
    thrust = 3236
    Cd = 2.07
    A = 1000.0
    m = 480000.0
    rho = 3.8e-12

    # Initial conditions
    R = R_EARTH + altitude
    pos = np.array([R, 0.0])
    vel = np.array([0.0, velocity])

    dt = 1.0
    total_time = time_minutes * 60
    interval = int(total_time / dt)

    positions = np.zeros((2, interval))

    for i in range(interval):
        
        r = np.linalg.norm(pos)
        u = pos / r

        
        g_mag = G * M_EARTH / r**2
        g_vec = -g_mag * u

        # Velocity magnitude and direction
        v = np.linalg.norm(vel)
        if v == 0:
            v_unit = np.zeros(2)
        else:
            v_unit = vel / v

        # Drag and thrust 
        drag = -0.5 * rho * Cd * A * v**2 * v_unit
        thrust_vec = -thrust * v_unit

        # vertical and horizontal accelaration
        acc = g_vec + (drag + thrust_vec) / m

        # motion
        vel += acc * dt
        pos += vel * dt
        
        positions[:, i] = pos

    # Plot results
    plot_position_earth(positions[0], positions[1])
    return positions[0], positions[1]

if __name__ == '__main__':
    final_burn(220000, 7770, 60)
    final_burn(220000, 0, 60)


