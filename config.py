#Consants
G =  1.0 #6.67430×10−11 but normalize
m = 1.0
M = 100.0

dt = 0.006
horizon_r = 2.0 #for newtonian version, if particle gets too close to black hole it gets "captured" //schwarzschild-like radius
num_steps = 20000

r0 = 6.0 #initial orbit radius

DEFAULT_PRESET = "circular"
DEFAULT_MODEL = "newtonian"
DEFAULT_INTEGRATOR = "verlet"