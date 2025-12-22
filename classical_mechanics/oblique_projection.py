import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def projectile_motion(state, t, m, k, g):
    x, y, vx, vy = state  
    ax = -(k/m) * vx
    ay = -g - (k/m) * vy
    return [vx, vy, ax, ay]

m = 1.0  
k = 0.2   
g = 9.8   

v0 = 20.0  
angle = 45.0 * (np.pi / 180) 

initial_state = [0.0, 0.0, v0 * np.cos(angle), v0 * np.sin(angle)]

t = np.linspace(0, 4, 100) 

sol = odeint(projectile_motion, initial_state, t, args=(m, k, g))
x_data = sol[:, 0]  
y_data = sol[:, 1]  

plt.figure(figsize=(8, 5))
plt.plot(x_data, y_data, label='Trajectory (with drag)')
plt.axhline(0, color='black', linewidth=1) 

plt.title('Projectile Motion with Air Resistance')
plt.xlabel('Distance (m)') 
plt.ylabel('Height (m)')    
plt.xlim(0, 40)             
plt.ylim(0, 15)
plt.grid()
plt.legend()
plt.show()