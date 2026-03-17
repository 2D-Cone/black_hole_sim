#Helpers
import numpy as np
from sympy.physics.units import velocity


def compute_acceleration_newtonian(position, G, M):
    #compute r
    r = np.linalg.norm(position)
    #return acceleration vector
    #a_vec = -((G * M)/r^3) * r_vec
    acceleration = -((G * M) / (r**3)) * position #position is the r_vec [x,y}
    return acceleration
    pass

def compute_energy_newtonian(position, velocity, G, M, m):
    #compute kinetic + potential
    #if velocity is v = [vx, vy] then v = sqrt(vx^2 + vy^2)
    speed = np.linalg.norm(velocity)
    kinetic = 0.5 * m * speed**2  #Kinetic = (1/2) * (mv^2)
    r = np.linalg.norm(position)  #distance from origin is r_vec
    potential = -(G * M * m) / r  #potential energy is U = -GMm/r
    total_energy = kinetic + potential
    return total_energy
    pass

def compute_acceleration_pw(position, G, M, horizon_r): #pw stands for Paczynski Witta
    #psuedo-newtonian black hole potential is Phi(r) = -GM/(r-r_s) where r_s is schwarzschild radius
    #here, we use horizon_r as the Schwarzschild-like radius r_s
    #vector acceleration for Paczynski Wiita is :
    #a_vec = -GM/(r*(r-r_s)^2) *r_vec

    r = np.linalg.norm(position)
    #no dividing by zero!
    if r <= horizon_r:
        return np.array([0.0, 0.0], dtype=float)

    acceleration = -((G*M)/r*(r - horizon_r)**2) * position #extra r* on bottom because need *r_vec/r to give normalized direction for force.  recall that position = r_vec
    return acceleration

def compute_energy_pw(position, G, M, horizon_r):
    speed = np.linalg.norm(velocity) #speed (scalar) is just length (magnitude) of velocity vector
    kinetic = 0.5 * M * speed**2  # (1/2)*(mv^2)

    r = np.linalg.norm(position)
    if r <= horizon_r:
        return float("-inf") #ruh roh raggy

    potential = -((G*M)/(r-horizon_r)**2)
    total_energy = kinetic + potential
    return total_energy






def compute_angular_momentum(position, velocity, m):
    #return scalar Lz
    #in 2d, Lz = m((x * vy) - (y * vx))
    #unpack those vecties
    x, y = position
    vx, vy = velocity
    return m * (x * vy - y * vx)
    pass


def get_physics_functions(model_name):
    if model_name == "newtonian":
        return compute_acceleration_newtonian, compute_energy_newtonian
    if model_name == "pw":
        return compute_acceleration_pw, compute_energy_pw
    raise ValueError("Unknown model_name: {model_name}")
