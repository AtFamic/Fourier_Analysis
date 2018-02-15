import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use("dark_background")
fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)

x0 = np.linspace(0,2,10000)

t0 = 0

dt = 0.01
# 時間間隔

h = 2
# 初期の高さ


a = []

def y(x,t):
    sigma = 0
    for n in range(50):
        sigma = sigma + (-1) **(n+1) / (2*n - 1) ** 2 * np.sin((2*n -1)*np.pi*x/2)*np.cos((2*n-1)*np.pi*t/2)
    return 8 * h / np.pi ** 2 * sigma

for i in range(5000):
    value = y(x0,t0)
    t0 = t0 + dt
    a.append(value)

k = 0

def _update_plot(i):
    global k
    x = a[k]
    k += 1
    ax1.clear()
    plt.plot(x0,x)
    plt.grid(True)
    plt.ylim([-h-2,h+2])
    plt.xlim([-1,3])



ani = animation.FuncAnimation(fig, _update_plot, frames=360, interval=20)
plt.show()

plt.show()