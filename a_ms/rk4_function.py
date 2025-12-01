import numpy as np

def rk4_step(function, x, v, dt):

    k1 = function(x, v)
    l1 = v

    k2 = function(x + 0.5*dt*l1, v + 0.5*dt*k1)
    l2 = v + 0.5*dt*k1

    k3 = function(x + 0.5*dt*l2, v + 0.5*dt*k2)
    l3 = v + 0.5*dt*k2

    k4 = function(x + dt*l3, v + dt*k3)
    l4 = v + dt*k3

    
    v_next = v + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)
    x_next = x + (dt/6)*(l1 + 2*l2 + 2*l3 + l4)

    return x_next, v_next