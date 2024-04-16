import numpy as np
import matplotlib.pyplot as plt

# number of steps
n_steps = 100000

# begin at the origin (0, 0)
x_pos = [0]
y_pos = [0]


# random steps
for _ in range(n_steps):
    # randomly choose up (+1) or down (-1) in y-axis
    dy = np.random.choice([-1,1])
    
    # update positions
    new_x = x_pos[-1] + 1  # move one step in the x-axis
    new_y = y_pos[-1] + dy # move dy in the y-axis
    x_pos.append(new_x)
    y_pos.append(new_y)
    


# plot the forward random walk
plt.plot(x_pos, y_pos, marker='o', linestyle='-', markersize=1, mec="r", linewidth=0.5)
plt.plot([0,_],[0,y_pos[-1]], color="black")
plt.title("2D Forward Random Walk [50% Up/Down]")
plt.xlabel("X Position")
plt.ylabel("Y Position")
plt.grid(True)
plt.show()

