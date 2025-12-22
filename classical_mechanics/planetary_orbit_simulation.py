import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def space(r, t, GM):
    x, y, vx, vy = r
    r3 = (x**2 + y**2 )**1.5
    ax = -GM * x / r3
    ay = -GM * y / r3
    return [vx, vy, ax, ay]

GM = 1.0
r0 = [1.0, 0.0, 0.0, 1.3]

# 時間を定義（円軌道なので 2π ≒ 6.3秒で1周します）
t = np.linspace(0, 200, 1000)

sol = odeint(space, r0, t, args=(GM,))

plt.figure(figsize=(10, 5)) 
plt.plot(sol[:, 0], sol[:, 1], label='Orbit')
plt.plot(0, 0, 'ro', label='Sun') 

plt.axis('equal') 
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()