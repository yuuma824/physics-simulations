import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. 物理モデル（空気抵抗のある投げ上げ）
# state の中身は [x座標, y座標, 横速度vx, 縦速度vy] の4つ！
def projectile_motion(state, t, m, k, g):
    x, y, vx, vy = state  # 4つにバラす
    
    # --- 加速度の計算 (F = ma より a = F/m) ---
    # 横方向: 空気抵抗のみ (-k * vx)
    ax = -(k/m) * vx
    
    # 縦方向: 重力(-g) + 空気抵抗(-k * vy)
    ay = -g - (k/m) * vy
    
    # [xの変化率, yの変化率, vxの変化率, vyの変化率]
    # つまり [vx, vy, ax, ay] を返す
    return [vx, vy, ax, ay]

# 2. パラメータ
m = 1.0   # ボールの重さ (kg)
k = 0.2   # 空気抵抗係数 (これがあると飛ばなくなる)
g = 9.8   # 重力加速度

# 3. 初期条件（斜め45度に思いっきり投げる）
v0 = 20.0  # 初速 (m/s)
angle = 45.0 * (np.pi / 180)  # 角度をラジアンに変換

# [x=0, y=0, vx=初速の横成分, vy=初速の縦成分]
initial_state = [0.0, 0.0, v0 * np.cos(angle), v0 * np.sin(angle)]

t = np.linspace(0, 4, 100) # 0秒〜4秒

# 4. 計算実行
sol = odeint(projectile_motion, initial_state, t, args=(m, k, g))

# 5. プロット（ここが重要！）
# 横軸を「時間」ではなく「距離(x)」にします
x_data = sol[:, 0]  # 0列目: x座標
y_data = sol[:, 1]  # 1列目: y座標

plt.figure(figsize=(8, 5))
plt.plot(x_data, y_data, label='Trajectory (with drag)')

# 地面を描く
plt.axhline(0, color='black', linewidth=1) 

plt.title('Projectile Motion with Air Resistance')
plt.xlabel('Distance (m)')  # 横軸は距離
plt.ylabel('Height (m)')    # 縦軸は高さ
plt.xlim(0, 40)             # 見やすいように範囲固定
plt.ylim(0, 15)
plt.grid()
plt.legend()
plt.show()