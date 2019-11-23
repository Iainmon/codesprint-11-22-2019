from src.sorts import *
from src.lib.historic_array import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



L = HistoricArray.randomized(10)
bubble_sort(L)


fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, len(L.list_states[i]), 1)
    y = np.array(L.list_states[i])
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(L.list_states), interval=20, blit=True)
plt.show()