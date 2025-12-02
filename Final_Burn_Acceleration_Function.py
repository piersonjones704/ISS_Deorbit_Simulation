import numpy as np
from c_ms.constants import *
import math

def final_burn_accel(pos, vel):
      thrust = 3236
      Cd = 2.07
      A = 1000.0
      m = 480000.0
      rho = 3.8e-12
      r = np.linalg.norm(pos)
      u = pos / r

        
      g_mag = G * M_EARTH / r**2
      g_vec = -g_mag * u

      v = np.linalg.norm(vel)
      if v == 0:
            v_unit = np.zeros(2)
      else:
            v_unit = vel / v


      drag = -0.5 * rho * Cd * A * v**2 * v_unit
      thrust_vec = -thrust * v_unit
      acc = g_vec + (drag + thrust_vec) / m
      return np.array([acc])
