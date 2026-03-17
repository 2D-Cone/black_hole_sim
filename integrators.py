# semi-implicit euler update!
# v_vec_new = v_vec + a_vec*dt
# r_vec_new = r_vec + v_vec_new*dt
def semi_implicit_euler_step(position, velocity, dt, acceleration_func, accel_kwargs):
    acceleration = acceleration_func(position, **accel_kwargs) #accel_kwargs will hold necessary acceleration arguments/variables/constants

    velocity = velocity + acceleration * dt
    position = position + velocity * dt

    return position, velocity

def verlet_velocity_step(position, velocity, dt, acceleration_func, accel_kwargs):
    acceleration_old = acceleration_func(position, **accel_kwargs)

    position_new = position + velocity * dt * (acceleration_old * dt**2) # just plugging in kinematic eqn p_new = p + v*dt + (a*dt^2)
    acceleration_new = acceleration_func(position_new, **accel_kwargs)

    velocity_new = velocity + 0.5*(acceleration_old + acceleration_new) * dt
    #above formula comes from v_new = v + a*dt where we integrate using trapezoidal integration for 'a' and get (a_old+a_new)/2
    return position_new, velocity_new