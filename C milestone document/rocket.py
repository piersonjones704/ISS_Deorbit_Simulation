from constants import *
from plot import plot_simple

wet_mass = M_0_LV
dry_mass = M_0_LV/MASS_RATIO_LV
burn_time = (wet_mass - dry_mass)/M_DOT_E_LV

def thrust(t):
    if t <= burn_time:
        return M_DOT_E_LV*I_SP_LV*g_0
    else:
        return 0
    
def air_density(h):
    return RHO_0*math.exp(-h/H_0)

def drag_force(v, h):
    return 1/2*air_density(h)*v*abs(v)*C_D_LV*AREA_LV

def m(t):
    mass = M_0_LV - M_DOT_E_LV*t
    if mass > dry_mass:
        return mass
    else:
        return dry_mass  
    
def grav_force(t, h):
    return (G*M_EARTH*m(t))/(R_EARTH + h)**2

def a(t, h, v):
    return (thrust(t) - drag_force(v, h) - grav_force(t, h))/m(t)

def approx(sim_time, t_step, h_0, v_0):
    t = 0.0
    h = h_0
    v = v_0
    length = int(sim_time/t_step) + 1
    t_plot = [0] * int(length)
    h_plot = [0] * int(length)
    v_plot = [0] * int(length)

    t_plot[0] = 0
    h_plot[0] = h_0
    v_plot[0] = v_0

    for i in range(1, len(t_plot)):
        v_plot[i] = v + t_step*a(t, h, v)
        v = v_plot[i]
        h_plot[i] = h + t_step*v
        h = h_plot[i]
        t_plot[i] = t_plot[i-1] + t_step
        t += t_step

        if h <= 0 and t > 0 or i == len(t_plot):
            h_plot[i] = 0
            v_plot[i] = v
            t_plot = t_plot[:i-1]
            h_plot = h_plot[:i-1]
            v_plot = v_plot[:i-1]
            break
    return t_plot, h_plot, v_plot, max(h_plot)
    

def main():
    # TODO: write me
    sim_time = 80*burn_time
    t_step = 0.1
    h_0 = 0
    v_0 = 0
    time, height, velocity, max = approx(sim_time, t_step, h_0, v_0)
    plot_simple(time, height)
    #plot_simple(time, velocity)
    
    

if __name__ == '__main__':
    main()
