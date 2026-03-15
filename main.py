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
    #return acceleration vector
    pass

def compute_angular_momentum(position, velocity, m):
    #return scalar Lz
    pass

def compute_energy(position, velocitt, G, M, m):
    #compute kinematic + potential
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