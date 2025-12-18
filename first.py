import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 運動方程式（単振り子の場合：d^2θ/dt^2 = - (g/L) * sin(θ)）
def pendulum_equations(y, t, g, L):
    theta, omega = y
    dydt = [omega, -(g/L) * np.sin(theta)]
    return dydt

# パラメータ設定
L = 1.0  # 紐の長さ
g = 9.8  # 重力加速度
y0 = [np.pi/4, 0.0]  # 初期状態（45度から静かに離す）
t = np.linspace(0, 10, 101)  # 0秒から10秒まで

# 微分方程式を解く（これが「ソルバー」です）
sol = odeint(pendulum_equations, y0, t, args=(g, L))

# グラフ化
plt.plot(t, sol[:, 0])
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.grid()
plt.show()