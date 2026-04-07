import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from simulation import Satellite
import numpy as np
from constants import G, M

# Two satellites
sat = Satellite(7e6, 0, 0, 7700)
sat2 = Satellite(8e6, 0, 0, 7200)

r1 = 7e6
r2 = 8e6

T1 = 2 * np.pi * np.sqrt(r1**3 / (G * M))
T2 = 2 * np.pi * np.sqrt(r2**3 / (G * M))

speed_factor= 1

fig, ax = plt.subplots()
ax.set_xlim(-1.2e7, 1.2e7)
ax.set_ylim(-1.2e7, 1.2e7)

ax.set_title("Satellite Orbit Simulation")
ax.set_aspect('equal')
ax.text(-1.1e7, 1.05e7, f"Orbit 1 Period: {T1:.1f} s", color='red')
ax.text(-1.1e7, 9.5e6, f"Orbit 2 Period: {T2:.1f} s", color='green')
ax.set_facecolor('black')
ax.legend(["Satellite 1", "Satellite 2"])
ax.set_axisbelow(True) 
ax.grid(True, color='gray', linestyle='--', linewidth=0.5, alpha=0.5, zorder=0)
fig.patch.set_facecolor('black')

# Earth
earth = plt.Circle((0, 0), 6.4e6, color='cyan')
ax.add_patch(earth)

# Satellites
point, = ax.plot([], [], 'ro', markersize=5)   # red
point2, = ax.plot([], [], 'go', markersize=5)  # green
ax.legend(loc="upper right") 

# Orbit paths
path1_x, path1_y = [], []
path2_x, path2_y = [], []

def update(frame):
    x1, y1 = sat.update(speed_factor)
    x2, y2 = sat2.update(speed_factor)

    # Store path
    path1_x.append(x1)
    path1_y.append(y1)

    path2_x.append(x2)
    path2_y.append(y2)

    # Update satellite positions
    point.set_data([x1], [y1])
    point2.set_data([x2], [y2])
    
    line1.set_data(path1_x, path1_y)  
    line2.set_data(path2_x, path2_y)

    return point, point2

ani = FuncAnimation(fig, update, frames=1000, interval=20)

plt.show()