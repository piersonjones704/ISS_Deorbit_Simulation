from constants import *
from plot import plot_position_earth
import math
import numpy as np

def final_burn(altitude, velocity, time_minutes):
    '''
    stage 2, this is the simulation of final burn.
    the function takes in starting altitude, starting velocity and a the chosen simulation time for this section of simulation.
    the function will then plot the tracjectory of the station and return the final position and final velocity of the station.
    '''
    # Constants
    thrust = 3236
    Cd = 2.07
    A = 1000.0
    m = 480000.0
    rho = RHO_0*np.exp(-(altitude/7500))

    # Initial conditions
    altitude = np.array([altitude[-1,:]])
    vel = np.array([[velocity[-1,:]]])
    pos = altitude[-1, :]
    vel = velocity[-1, :]

    dt = 1.0
    total_time = time_minutes * 60
    interval = int(total_time / dt)
    times = np.zeros(interval)
    velocities = np.zeros((interval, 2))
    positions = np.zeros((interval, 2))

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
        times[i] = i * dt
        
        positions[i, :] = pos
        velocities[i, :] = vel
        r = np.linalg.norm(pos)
        if r <= R_EARTH:
            status = 'hit ground'
            positions = positions[:i+1]
            velocities = velocities[:i+1]
            times = times[:i+1]
            return positions, velocities, times, status


    # Plot results
    # plot_position_earth(positions[:, 0], positions[:, 1])
    status = 'orbiting or escaped orbit'
    return positions, velocities, times, status
    

#if __name__ == '__main__':
    


