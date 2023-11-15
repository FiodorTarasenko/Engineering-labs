import numpy as np
import matplotlib.ticker as ticker
from matplotlib.lines import Line2D
from scipy import signal
import matplotlib.pyplot as plt
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
plt.plot(time, pressure, linewidth=0.7, color='orange')
plt.scatter(7.8381424, 119.10755561, s=10, color='red')
plt.scatter(17.613132, 72.21096292, s=10, color='red')
tick_spacing_x = 0.5
tick_spacing_y = 5
xl = np.arange(7.5, 22.5, 2.5)
yl = np.arange(40, 140.0, 20)
plt.ylim(50, 135)
plt.xlim(5, 22.5)
ax.xaxis.set_major_locator(ticker.FixedLocator(xl))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_x))
ax.yaxis.set_major_locator(ticker.FixedLocator(yl))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_y))
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", color='lightgrey', linewidth=0.5, linestyle='--')
ax.set_title('Артериальное давление \n до физической нагрузки', fontdict={'fontsize':10.0})
ax.set_xlabel('Время [c]', fontdict={'fontsize':10.0})
ax.set_ylabel('Давление [мм рт. ст.]', fontdict={'fontsize':10.0})
ax.text(7.8381424, 120, 'Systole', fontdict={'fontsize':10.0})
ax.text(17.613132, 73, 'Diastole', fontdict={'fontsize':10.0})
#line1, = ax.plot(time, pressure, label='Line 1')
legend_elements = [Line2D([0], [0], color='orange', linewidth=0.7, label='Давление - 119/73[мм рт. ст.]')]
ax.legend(handles=legend_elements)
fig.savefig('graph.png')
plt.show()