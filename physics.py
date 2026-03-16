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
