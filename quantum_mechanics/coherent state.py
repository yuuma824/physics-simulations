import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_min, x_max = -10, 10
num_points = 1000
x = np.linspace(x_min, x_max, num_points)

t_max = 20  
dt = 0.05   
times = np.arange(0, t_max, dt)

alpha_0 = 3.0 + 0.0j  

def potential(x):
    
    return 0.5 * x**2

def coherent_probability_density(x, t, alpha_0):
   
    alpha_t = alpha_0 * np.exp(-1j * t)

    x_center = np.sqrt(2) * np.real(alpha_t)
    
    density = (1 / np.sqrt(np.pi)) * np.exp(- (x - x_center)**2)
    
    return density, x_center

fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(x_min, x_max)
ax.set_ylim(0, 1.2)  
ax.set_xlabel("Position x")
ax.set_ylabel("Probability Density |ψ|² / Potential V")
ax.set_title("Simulation of a Quantum Coherent State")
ax.grid(True)

ax.plot(x, potential(x) / 10, 'k--', label='Potential V(x) (scaled)', alpha=0.5)

density_line, = ax.plot([], [], 'b-', linewidth=2, label='Probability Density |ψ|²')
center_point, = ax.plot([], [], 'ro', label='Center <x>')
time_text = ax.text(0.05, 0.95, '', transform=ax.transAxes)

ax.legend(loc='upper right')

def animate(frame_idx):
    t = times[frame_idx]
    
    density, x_c = coherent_probability_density(x, t, alpha_0)
    
    density_line.set_data(x, density)
    center_point.set_data([x_c], [coherent_probability_density(x_c, t, alpha_0)[0]])
    time_text.set_text(f'Time = {t:.2f}')
    
    return density_line, center_point, time_text

anim = FuncAnimation(fig, animate, frames=len(times), interval=30, blit=True)

plt.show()