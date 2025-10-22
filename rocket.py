from constants import *
from plot import plot_simple

t = 0.0
h = 0.0
v = 0.0
t_plot = []
h_plot = []
v_plot = []

def thrust(t)
    wet_mass = M_0_LV
    dry_mass = M_0_LV/MASS_RATIO_LV
    burn_time = (wet_mass - dry_mass)/M_DOT_E_LV
    if t > burn_time:
        return 0
    else:
        return M_DOT_E_LV*I_SP_LV*g_0
    
def air_density(h)
    return RHO_0*math.exp(-h/H_0)

def drag(v, h):
    return 1/2*air_density(h)*v*abs(v)*C_D_LV*AREA_LV

def main():
    # TODO: write me
    


if __name__ == '__main__':
    main()
