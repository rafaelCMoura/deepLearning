# Simple 1D Upwind FDM discretization

import numpy as np

# Spatial discretization
L = 10.0                                      # Domain length
n = 21                                        # Number of points
dx = L/(n-1)                                  # Length of spacing

# Time discretization
nt = 2                                        # Number of time steps
dt = 0.1                                      # Time step

# Wave equation parameters
a = 0.5                                       # Velocity coefficient

# Initial conditions
f = np.zeros((n,1))                           # Wave function (Initialization)
f[4:9] = 1.0                                  # Wave square pulse

print f
f_old = f
# Time loop
for k in range(0,nt):
    for i in range(1,n-1):
        f[i] = f_old[i] - (a*dt/dx)*(f_old[i]-f_old[i-1])
    f[0] = f_old[n-1]
    f_old = f
    print f         # TODO: matplotlib fig save here
