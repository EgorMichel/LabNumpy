import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

U = np.loadtxt("Third/data.txt")
A = np.eye(len(U))
A[np.arange(U.shape[0]), np.arange(U.shape[0])-1] = -1

fig = plt.figure()
ax = plt.axes(xlim=(0, len(U)), ylim=(0, max(U)))
ax.grid()
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def animate(n):
    global U
    x = np.linspace(0, len(U))
    if n == 0:
        line.set_data(x, U)
        return line,
    U = U - 0.5 * A @ U
    line.set_data(x, U)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=255, interval=50, blit=True)

anim.save('animation.gif')
