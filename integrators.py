# semi-implicit euler update!
# v_vec_new = v_vec + a_vec*dt
# r_vec_new = r_vec + v_vec_new*dt
def semi_implicit_euler_step(position, velocity, acceleration, dt):
    velocity = velocity + acceleration * dt
    position = position + velocity * dt
    return position, velocity