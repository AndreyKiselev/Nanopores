#!/usr/bin/python
# -*- coding: utf8 -*-
import numpy as np
import scipy
from scipy import signal
from scipy.fftpack import fft


import matplotlib.pyplot as plt

Initial = 40
Resampled = 5

x_0 = np.linspace(0, 5, Initial)
y_0 = np.sin(x_0)
x_1 = np.linspace(0, 5, Initial)
#y_1 = np.sin(x_1)+np.random.normal(0, 0.05, Initial) 
y_1 = np.sin(x_1)+0.1 * np.sin(10 * x_1) 
#x_2 = np.linspace(0, 5, Resampled)
#y_2 = scipy.signal.resample(y_1, Resampled)

Wn = 0.4
b, a = signal.bessel(4, Wn, btype='low', analog=False)
output = signal.filtfilt(b, a, y_1)
x_3 = np.linspace(0, 5, len(output))
print(len(output))
#plt.plot(x_0,y_0, '.', x_1, y_1, x_3, output, 'bs')

output_ftt = np.ftt()
plt.grid()
plt.show()
