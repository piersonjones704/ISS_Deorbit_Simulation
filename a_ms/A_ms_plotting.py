import numpy as np
from constants import *
import matplotlib.pyplot as plt


def plot_final_simulation(pos, time, od_steps, fb_steps, separation_pos, impact_pos, rocket_pos, rocket_time):
    """Creates two plots, Left: Map view of ISS trajectory (orbital decay, final burn, reentry), and Right: Altitude vs. time for rocket launch. 
    This function returns 2 subplots"""
    # Create figure with 2 subplots
    fig, (ax_map, ax_alt) = plt.subplots(1, 2, figsize=(12, 5))
    
    # ISS Map View Plot
    pos = np.asarray(pos)
    N = len(pos)
    od_end = min(int(od_steps), N-1)
    fb_end = min(od_end + int(fb_steps), N-1)
    
    # Split position array into phases
    pos_od = pos[0:od_end+1]
    pos_fb = pos[od_end:fb_end+1]
    pos_re = pos[fb_end:]
    
    # Draw Earth
    theta = np.linspace(0, 2*np.pi, 200)
    ax_map.plot(R_EARTH*np.cos(theta), R_EARTH*np.sin(theta), color='0.7', linewidth=2)
    
    # Helper function to plot trajectory phases
    def plot_phase(array, color, label):
        if len(array):
            ax_map.plot(array[:, 0], array[:, 1], color = color[0], linewidth=1.5)
            ax_map.plot(array[0, 0], array[0, 1], 'o', color = color[0], markersize=8)
            ax_map.plot(array[-1, 0], array[-1, 1], '^', color = color[0], markersize=8)
    
    # Plot ISS trajectory phases
    plot_phase(pos_od, 'g-', 'orbital decay')
    plot_phase(pos_fb, 'r-', 'final burn')
    plot_phase(pos_re, 'k-', 'reentry')
    
    # Mark separation and impact points
    if separation_pos is not None:
        ax_map.plot(separation_pos[0], separation_pos[1], 'ms', markersize=10, 
                   label='separation (100 km)', markeredgewidth=2)
    if impact_pos is not None:
        ax_map.plot(impact_pos[0], impact_pos[1], 'kx', markersize=12, 
                   markeredgewidth=3, label='impact')
    
    ax_map.set_aspect('equal')
    ax_map.set_xlabel('x (m)', fontsize=11)
    ax_map.set_ylabel('y (m)', fontsize=11)
    ax_map.set_title('ISS Trajectory', fontsize=13, fontweight='bold')
    ax_map.legend(loc='best', fontsize=9)
    ax_map.grid(True)
    
    # Rocket Altitude vs. Time plot
    ax_alt.plot(rocket_time, rocket_pos, 'b-', linewidth=2)
    ax_alt.set_xlabel('Time (s)', fontsize=11)
    ax_alt.set_ylabel('Altitude (km)', fontsize=11)
    ax_alt.set_title('Rocket Launch Trajectory', fontsize=13, fontweight='bold')
    ax_alt.grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return fig, (ax_map, ax_alt)