import numpy as np
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from scipy import signal
import matplotlib.pyplot as plt
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
data_y = pressure
data_x = time
print(pressure)
# Фильтрация низких частот
fs = 1000  # Частота дискретизации
cutoff = 10  # Частота среза
order = 5  # Порядок фильтра
nyquist = 0.5 * fs
normal_cutoff = cutoff / nyquist
b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
filtered_signal = signal.lfilter(b, a, pressure)
pressure = filtered_signal
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
ax = plt.gca()
plt.plot(time, pressure, linewidth=0.7, color='blue')
plt.scatter(10.87003994, 117.34348443, s=10, color='red')
plt.scatter(28.5377028, 79.77653534, s=10, color='red')
tick_spacing_x = 0.5
tick_spacing_y = 5
xl = np.arange(2.5, 35.0, 5)
yl = np.arange(60, 140.2, 20)
plt.ylim(55, 140)
plt.xlim(4, 35)
ax.xaxis.set_major_locator(ticker.FixedLocator(xl))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_x))
ax.yaxis.set_major_locator(ticker.FixedLocator(yl))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_y))
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", color='lightgrey', linewidth=0.5, linestyle='--')
ax.set_title('Артериальное давление \n до физической нагрузки', fontdict={'fontsize':10.0})
ax.set_xlabel('Время [c]', fontdict={'fontsize':10.0})
ax.set_ylabel('Давление [мм рт. ст.]', fontdict={'fontsize':10.0})
ax.text(10.87003994, 120, 'Systole', fontdict={'fontsize':10.0})
ax.text(28.5377028, 81, 'Diastole', fontdict={'fontsize':10.0})
#line1, = ax.plot(time, pressure, label='Line 1')
legend_elements = [Line2D([0], [0], color='blue', linewidth=0.7, label='Давление - 118/80 [мм рт. ст.]')]
ax.legend(handles=legend_elements)
fig.savefig('graph.png')
plt.show()