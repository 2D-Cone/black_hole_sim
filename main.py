import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

#Consants
G =  1.0 #6.67430×10−11 but normalize
m = 1.0
M = 1.0
dt = 0.01
horizon_r = 2.0 #for newtonian version, if particle gets too close to black hole it gets "captured"
num_steps = 5000

#Initial conditions
r0 = 8.0 #initial orbit radius
position = np.array([r0, 0.0], dtype=float)
v_circ = np.sqrt((G * M)/r0) #vcirc = sqrt((G * M)/r0))
velocity = np.array([0.0, v_circ], dtype=float) #perpendicular motion to position (x, ..) vs (.., y)


#Helpers
def compute_acceleration(position, G, M):
    #compute r
    r = np.linalg.norm(position)
    #return acceleration vector
    #a_vec = -((G * M)/r^3) * r_vec
    acceleration = -((G * M) / (r**3)) * position #position is the r_vec [x,y}
    return acceleration
    pass

def compute_energy(position, velocity, G, M, m):
    #compute kinetic + potential
    #if velocity is v = [vx, vy] then v = sqrt(vx^2 + vy^2)
    speed = np.linalg.norm(velocity)
    kinetic = 0.5 * m * speed**2  #Kinetic = (1/2) * (mv^2)
    r = np.linalg.norm(position)  #distance from origin is r_vec
    potential = -(G * M * m) / r  #potential energy is U = -GMm/r
    total_energy = kinetic + potential
    return total_energy
    pass

def compute_angular_momentum(position, velocity, m):
    #return scalar Lz
    #in 2d, Lz = m((x * vy) - (y * vx))
    #unpack those vecties
    x, y = position
    vx, vy = velocity
    return m * (x * vy - y * vx)
    pass


#history_cont
x_history = []
y_history = []
time_history = []
energy_history = []
angular_momentum_history = []

#main sim loop
captured = False

for step in range(num_steps)
    #record history

    #compute acceleration

    #semi-implicit Euler update?

    #check horizon cross
    #if captured: break


#plot trajectory
fig,ax = plt.subplots()


#plot trajectory
#plot black hole
#set equal aspect ratio
#labels, title, grid
plt.show()