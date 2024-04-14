import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# set the number of steps
n_steps = 1000

# start at the origin (0, 0)
x_pos = [0]
y_pos = [0]
z_pos = [0]

# create the random steps
for _ in range(n_steps):
    
    # generate random step sizes
    # for simplicity we assume a normal distribution
    dx, dy, dz = np.random.normal(0, 1, 3)
    
    # update positions
    x_new = x_pos[-1] + dx
    y_new = y_pos[-1] + dy
    z_new = z_pos[-1] + dz
    
    x_pos.append(x_new)
    y_pos.append(y_new)
    z_pos.append(z_new)

# plot the random walk
#ax.figure(figsize=(8, 6))
ax.plot(x_pos, y_pos, z_pos, marker='o', linestyle='-', markersize=2, linewidth=0.5, mec="r")
plt.title("3D Random Walk")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.grid(True)
plt.show()
