import numpy as np
from matplotlib import pyplot as plt
import os

fig, ax = plt.subplots(len(os.listdir("Second")), 2, figsize=(18, 12))
counter = 0
for file in os.listdir("Second"):
    data = np.loadtxt(os.path.join("Second", file))
    ax[counter, 0].plot(np.arange(0, len(data)), data)
    ax[counter, 0].set_title(file[:-4])

    new_data = np.convolve(data, np.ones(10), mode='valid') / 10
    ax[counter, 1].plot(np.arange(0, len(new_data)), new_data)
    ax[counter, 1].set_title(file[:-4])
    counter += 1

plt.savefig("22.png")
plt.show()

