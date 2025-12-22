import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. 物理ルール：星が3つある世界
def three_body_equations(w, t, G, m):
    # w（今の状態）には12個の数字が入っています
    # 星1: r1=[x1, y1], v1=[vx1, vy1]
    # 星2: r2=[x2, y2], v2=[vx2, vy2]
    # 星3: r3=[x3, y3], v3=[vx3, vy3]
    
    # わかりやすく12個の変数にバラします
    x1, y1, vx1, vy1 = w[0:4]
    x2, y2, vx2, vy2 = w[4:8]
    x3, y3, vx3, vy3 = w[8:12]
    
    # 距離の計算関数 (r = √dx^2+dy^2 の3乗)
    def get_r3(xi, yi, xj, yj):
        dx = xj - xi
        dy = yj - yi
        dist = np.sqrt(dx**2 + dy**2)
        return dist**3

    # それぞれの距離の3乗を計算
    r12_3 = get_r3(x1, y1, x2, y2) # 星1と星2
    r13_3 = get_r3(x1, y1, x3, y3) # 星1と星3
    r23_3 = get_r3(x2, y2, x3, y3) # 星2と星3
    
    # 加速度の計算 (万有引力 F = G*m*m / r^2)
    # 星1への力（星2と星3から引っ張られる）
    ax1 = G * m * (x2 - x1) / r12_3 + G * m * (x3 - x1) / r13_3
    ay1 = G * m * (y2 - y1) / r12_3 + G * m * (y3 - y1) / r13_3
    
    # 星2への力（星1と星3から引っ張られる）
    ax2 = G * m * (x1 - x2) / r12_3 + G * m * (x3 - x2) / r23_3
    ay2 = G * m * (y1 - y2) / r12_3 + G * m * (y3 - y2) / r23_3

    # 星3への力（星1と星2から引っ張られる）
    ax3 = G * m * (x1 - x3) / r13_3 + G * m * (x2 - x3) / r23_3
    ay3 = G * m * (y1 - y3) / r13_3 + G * m * (y2 - y3) / r23_3
    
    # 結果を返す（速度と加速度を交互に）
    return [vx1, vy1, ax1, ay1, 
            vx2, vy2, ax2, ay2, 
            vx3, vy3, ax3, ay3]

# 2. パラメータと初期条件（8の字を描く魔法の数字）
G = 1.0
m = 1.0

# Chenciner & Montgomery (2000) の解
x_pos = 0.97000436
y_pos = -0.24308753
vx_val = 0.46620368
vy_val = 0.43236573

# 星1, 星2, 星3 の [x, y, vx, vy] を全部つなげる
r0 = [x_pos, y_pos, -0.5*vx_val, -0.5*vy_val,    # 星1
      -x_pos, -y_pos, -0.5*vx_val, -0.5*vy_val,  # 星2
      0, 0, vx_val, vy_val]                      # 星3

# --- ここから下を書いてみよう！ ---
# 1. 時間 t を作る
# 2. odeint で計算する (args=(G, m) を忘れずに！)
# 3. plt.plot で3つの星を描く
#　未完成