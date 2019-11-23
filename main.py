from src.sorts import *
from src.lib.historic_array import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np



L = HistoricArray.randomized(30)
fast_sort(L)


fig = plt.figure()
ax = plt.axes(xlim=(-1, len(L.items)), ylim=(0, 1.2*len(L.items)))
bar = plt.bar(np.arange(len(L.items)), np.zeros((len(L.items))), width=1)

def animate(i):
    y_heights = np.array(L.list_states[i].list_snapshot)
    changed_key = L.list_states[i].key_changed
    accessed_key = L.list_states[i].key_accessed
    i = 0
    for rect, y in zip(bar, y_heights):
        rect.set_height(y)
        if changed_key == i:
            rect.set_color('r')
        elif accessed_key == i:
            rect.set_color('g')
        else:
            rect.set_color('b')
        i += 1
    return bar

anim = animation.FuncAnimation(fig, animate,
                               frames=len(L.list_states), interval=300, blit=True, repeat=False)
plt.show()