import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use("dark_background")
fig = plt.figure()
fig.set_dpi(100)
ax1 = fig.add_subplot(1,1,1)

x0 = np.linspace(0,20,1000)

t0 = 0

dt = 0.05
# 時間間隔

c = 2


a = []

def y(x,t):
    result = []
    x_axis = list(x)
    for i in range(len(x_axis)):
        if c * (t-1) <= x_axis[i] and x_axis[i] <= c * t:
            result.insert(i, np.sin(np.pi * (t - x_axis[i] / c)))
        if x_axis[i] < c *(t-1) or c * t < x_axis[i]:
            result.insert(i, 0)
    return result

for i in x0:
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
    plt.ylim([-1,2])
    plt.xlim([0,20])



ani = animation.FuncAnimation(fig, _update_plot, frames=360, interval=20)
plt.show()

plt.show()