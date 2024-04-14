import numpy as np
import matplotlib.pyplot as plt

# set the number of steps
n_steps = 1000

# start at the origin (0, 0)
x_pos = [0]
y_pos = [0]

# create the random steps
for _ in range(n_steps):
    
    # generate random step sizes
    # for simplicity we assume a normal distribution
    dx, dy = np.random.normal(0, 1, 2)
    
    # update positions
    x_new = x_pos[-1] + dx
    y_new = y_pos[-1] + dy
    
    x_pos.append(x_new)
    y_pos.append(y_new)

# plot the random walk
plt.figure(figsize=(8, 6))
plt.plot(x_pos, y_pos, marker='o', linestyle='-', markersize=2, linewidth=0.5, mec="r")
plt.title("2D Random Walk")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.show()
