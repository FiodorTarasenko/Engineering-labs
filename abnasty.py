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
# Фильтрация низких частот
fs = 1000  # Частота дискретизации
cutoff = 7  # Частота среза
order = 8  # Порядок фильтра
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
filtered_signal = signal.lfilter(b, a, pressure)
pressure = filtered_signal
lower_limit = 92
upper_limit = 105
lower_limit_time = 11
upper_limit_time = 13.75
indices = np.where((pressure >= lower_limit) & (pressure <= upper_limit))
pressure = pressure[indices[0]]
time = time[indices[0]]
def mapping(x, a, b):
    return a * x + b
popt, _ = curve_fit(mapping, time, pressure)
a, b = popt
new_x = time
new_y = mapping(new_x, a, b)
pressure -= new_y
maxima = pressure
time_m = time
for i in range(3):
    maxima_indices = argrelextrema(maxima, np.greater, order=1)
    maxima = maxima[maxima_indices]
    time_m = time_m[maxima_indices]
a_data = [0.23920703, 0.08721725, -0.04306536, 0.12260938]
maximtime = []
for i in range(len(maxima)):
    maximtime.append(maxima[i])
    maximtime.append(time_m[i])
maximtime=np.array(maximtime)
print(maximtime)
a_time = [11.04621816, 11.78296995, 12.48513269, 13.16295481]
a_time = [str(i) for i in a_time]
with open('a_timenasty.txt', 'w') as f:
    f.write('\n'.join(a_time))



print(len(maxima))
print(maxima)
print(a_data)

plt.plot(time_m, maxima, linewidth=0.5, color='red')
plt.plot(time, pressure)
plt.xlim(11, 13.75)
plt.ylim(-1.5, 1.5)
plt.show()