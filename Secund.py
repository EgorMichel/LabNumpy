import numpy as np
from matplotlib import pyplot as plt
import os


def function(item):
    index = np.where(data == item)[0][0]
    if 0 < index <= 10:
        item = data[:index].mean()
    elif index > 10:
        item = data[index - 10:index].mean()
    return item


fig, ax = plt.subplots(len(os.listdir("Second")), 2, figsize=(18, 12))

func = np.vectorize(function)
counter = 0
for file in os.listdir("Second"):
    data = np.loadtxt(os.path.join("Second", file))
    ax[counter, 0].plot(np.arange(0, len(data)), data)
    ax[counter, 0].set_title(file[:-4])

    new_data = func(data)
    ax[counter, 1].plot(np.arange(0, len(new_data)), new_data)
    ax[counter, 1].set_title(file[:-4])
    counter += 1

plt.show()
