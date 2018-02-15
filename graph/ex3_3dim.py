import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

fig = plt.figure()
ax = plt.axes(projection="3d")

x = np.arange(-np.pi,np.pi,0.01)
y = np.arange(-np.pi,np.pi,0.01)
z = 0
for n in range(100):
    z = z + np.cos(2*n*x) / (4*n ** 2 - 1)


k = 1/np.pi + np.sin(x) / 2 - 2/ np.pi * z

plt.plot(x,y,k)

plt.show()
