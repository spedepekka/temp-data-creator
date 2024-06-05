import numpy as np
import matplotlib.pyplot as plt

cycles = 2 # how many sine cycles
resolution = 25 # how many datapoints to generate

length = np.pi * 2 * cycles
my_wave = np.sin(np.arange(0, length, length / resolution))
plt.plot(my_wave)
plt.show()

