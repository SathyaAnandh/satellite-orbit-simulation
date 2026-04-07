import numpy as np
from constants import G, M

class Satellite:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def update(self, dt):
        r = np.sqrt(self.x**2 + self.y**2)

        ax = -G * M * self.x / r**3
        ay = -G * M * self.y / r**3

        self.vx += ax * dt
        self.vy += ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

        return self.x, self.y