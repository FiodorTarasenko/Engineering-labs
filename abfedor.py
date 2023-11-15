import numpy as np
from scipy.signal import argrelextrema
from scipy import signal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
pressure = np.loadtxt(r'C:\Users\marat\Desktop\pulse\datafedorpokoy1.txt')
time = np.loadtxt(r'C:\Users\marat\Desktop\pulse\timepokoyfedoralone1.txt')
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
order = 7  # Порядок фильтра
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
k, l = signal.butter(order, normal_cutoff, btype='low', analog=False)
filtered_signal = signal.lfilter(k, l, pressure)
pressure = filtered_signal
lower_limit = 87
upper_limit = 100
lower_limit_time = 18.9
upper_limit_time = 23.5
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
print(pressure)
maxima = pressure
time_m = time
for i in range(3):
    maxima_indices = argrelextrema(maxima, np.greater, order=1)
    maxima = maxima[maxima_indices]
    time_m = time_m[maxima_indices]
a_data = []
maximtime = []
for i in range(len(maxima)):
    maximtime.append(maxima[i])
    maximtime.append(time_m[i])
maximtime=np.array(maximtime)
print(maximtime)
a_time = []
a_time = [str(i) for i in a_time]
#with open('a_timenasty.txt', 'w') as f:
    #f.write('\n'.join(a_time))



print(len(maxima))
print(maxima)
a_data = [19.26760626, 20.33116961, 21.58517933, 22.79099035]
a_data = [str(i) for i in a_data]
#with open('b_timefedor.txt', 'w') as f:
    #f.write('\n'.join(a_data))
print(a_data)

plt.plot(time_m, maxima, linewidth=0.5, color='red')
plt.plot(new_x, new_y)
plt.plot(time, pressure)
plt.xlim(18.7, 23.2)
plt.ylim(-2, 2)
plt.show()