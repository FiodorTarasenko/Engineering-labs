import numpy as np
from scipy.signal import argrelextrema
from scipy import signal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
pressure = np.loadtxt(r'C:\Users\marat\Desktop\pulse\datanastypokoy.txt')
time = np.loadtxt(r'C:\Users\marat\Desktop\pulse\timepokoynastyalone.txt')
#
#
#
#Блок калибровки
o = []
with open(r'C:\Users\marat\Desktop\pulse\coefficients.txt') as f:
    for line in f:
        o.append(float(line))
k = o[0]
c = o[1]
pressure = (pressure - c) / k
#Конец блока калибровки
#
#
#
time_start = time[0]
time_end = time[1]
time = np.linspace(time_start, time_end, len(pressure)) - time_start
tmp = time
data_y = pressure
data_x = time
print(pressure)
# Фильтрация низких частот
fs = 1000  # Частота дискретизации
cutoff = 10  # Частота среза
order = 8  # Порядок фильтра
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
filtered_signal = signal.lfilter(b, a, pressure)
pressure = filtered_signal
for i in range(2):
    maxima_indices = argrelextrema(pressure, np.greater, order=1)
    pressure = pressure[maxima_indices]
    time = time[maxima_indices]
pressure_min = filtered_signal
time_min = tmp
for i in range(2):
    minima_indices = argrelextrema(pressure_min, np.less, order=1)
    pressure_min = pressure_min[minima_indices]
    time_min = time_min[minima_indices]
print('length of pressure_min=', len(pressure_min))
plt.plot(time, pressure, linewidth=0.2)
plt.plot(data_x[400:], filtered_signal[400:], linewidth=0.4, color='green')
plt.plot(time_min, pressure_min, linewidth=0.2)
plt.ylim(92, 105)
plt.xlim(11, 13.75)
print(filtered_signal)
print(len(filtered_signal))
lower_limit = 110
upper_limit = 120
lower_limit_dia = 70
upper_limit_dia = 80
indices = np.where((pressure >= lower_limit) & (pressure <= upper_limit))
print(indices)
print(pressure[indices[0]])
print(time[indices[0]])
indices = np.where((pressure >= lower_limit_dia) & (pressure <= upper_limit_dia))
print(pressure[indices[0]])
print(time[indices[0]])
plt.show()