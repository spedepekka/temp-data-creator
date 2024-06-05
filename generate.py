import numpy as np
import matplotlib.pyplot as plt

# One year of temperatures is somewhat a single sive wave
cycles = 1
# How many measurements in a timeframe?
# Once per hour for a year
resolution = 365 * 24
# From -1..1 to -30..30 which is quite good estimate for temperatures in Finland
temp_amplitude = 30

length = np.pi * 2 * cycles

number_of_points = length / resolution

# Plain sine wave
sine_wave = np.sin(np.arange(0, length, number_of_points))

# Fix amplitude of the wave or the temperatures
f = lambda x: x * temp_amplitude
sine_wave = f(sine_wave)

# Add a bit variation to measurements
randoms = np.random.normal(0.0, 0.2, len(sine_wave))
sine_wave = np.add(sine_wave, randoms)

plt.plot(sine_wave)
plt.show()
