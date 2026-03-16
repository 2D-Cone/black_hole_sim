import numpy as np
from config import G, M, m, dt, horizon_r, num_steps, r0
from physics import compute_acceleration, compute_energy, compute_angular_momentum
from integrators import semi_implicit_euler_step
from plotting import plot_trajectory, plot_diagnostics
from render_pygame import animate_pygame
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation


#Initial conditions
position = np.array([r0, 0.0], dtype=float)
v_circ = np.sqrt((G * M)/r0) #vcirc = sqrt((G * M)/r0))
velocity = np.array([0.0, v_circ], dtype=float) #perpendicular motion to position (x, ..) vs (.., y)

#history_cont
x_history = []
y_history = []
time_history = []
energy_history = []
angular_momentum_history = []
radius_history = []
speed_history = []

#main sim loop
captured = False

for step in range(num_steps):
    #record history
    x_history.append(position[0])
    y_history.append(position[1])
    time_history.append(step * dt)

    r_current = np.linalg.norm(position)
    speed_current = np.linalg.norm(velocity)

    radius_history.append(r_current)
    speed_history.append(speed_current)
    energy_history.append(compute_energy(position, velocity, G, M, m))
    angular_momentum_history.append(compute_angular_momentum(position, velocity, m))


    #compute acceleration
    acceleration = compute_acceleration(position, G, M)

    position, velocity = semi_implicit_euler_step(position, velocity, acceleration, dt)

    #check horizon cross
    r = np.linalg.norm(position)    #compute new radius
    #if captured: break
    if r <= horizon_r:
        captured = True
        break

data = {
    "x": x_history,
    "y": y_history,
    "time": time_history,
    "energy": energy_history,
    "L": angular_momentum_history,
    "radius": radius_history,
    "speed": speed_history,
    "captured": captured,
    "horizon_r": horizon_r,
}

#optional matplotlib figures
# plot_trajectory(data)
# plot_diagnostics(data)

#pygame playback
animate_pygame(data)