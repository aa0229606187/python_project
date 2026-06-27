import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

# 設定中文字型（macOS 使用 Heiti TC，Windows 使用 Microsoft JhengHei）
plt.rcParams['font.sans-serif'] = ['Heiti TC', 'Microsoft JhengHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示異常

# 產生 X 軸數據：0 到 4π，共 500 個點
x = np.linspace(0, 4 * np.pi, 500)

# 初始參數
A_init = 1.0      # 振幅
omega_init = 1.0  # 角頻率
phi_init = 0.0    # 相位偏移

# 建立圖表
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)  # 預留下方空間給滑桿

# 繪製初始波形
sin_line, = ax.plot(x, A_init * np.sin(omega_init * x + phi_init),
                    label='y = A·sin(ωx + φ)', color='#1f77b4')
cos_line, = ax.plot(x, A_init * np.cos(omega_init * x + phi_init),
                    label='y = A·cos(ωx + φ)', color='#ff7f0e')

# 設定圖表屬性
ax.set_title('正弦與餘弦波形互動繪圖', fontsize=14)
ax.set_xlabel('x (弧度)', fontsize=12)
ax.set_ylabel('y', fontsize=12)
ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-5, 5)
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right')

# 建立三個滑桿的座標 [left, bottom, width, height]
slider_color = 'lightgoldenrodyellow'

ax_amp = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=slider_color)
ax_freq = plt.axes([0.15, 0.10, 0.65, 0.03], facecolor=slider_color)
ax_phase = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=slider_color)

slider_amp = Slider(ax=ax_amp, label='振幅 A', valmin=0.1, valmax=5.0, valinit=A_init)
slider_freq = Slider(ax=ax_freq, label='頻率 ω', valmin=0.1, valmax=10.0, valinit=omega_init)
slider_phase = Slider(ax=ax_phase, label='相位 φ', valmin=0, valmax=2 * np.pi, valinit=phi_init)


def update(val):
    """滑桿回呼函式：取得目前滑桿數值並更新波形"""
    A = slider_amp.val
    omega = slider_freq.val
    phi = slider_phase.val

    sin_line.set_ydata(A * np.sin(omega * x + phi))
    cos_line.set_ydata(A * np.cos(omega * x + phi))

    fig.canvas.draw_idle()


# 註冊滑桿事件
slider_amp.on_changed(update)
slider_freq.on_changed(update)
slider_phase.on_changed(update)

plt.show()
