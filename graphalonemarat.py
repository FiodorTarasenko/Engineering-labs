import numpy as np
import matplotlib.ticker as ticker
from scipy import signal
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
pressure = np.loadtxt(r'C:\Users\marat\Desktop\pulse\datamaratpokoy.txt')
time = np.loadtxt(r'C:\Users\marat\Desktop\pulse\timepokoymaratalone.txt')
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
lower_limit = 85
upper_limit = 100
lower_limit_time = 10.0
upper_limit_time = 20.5
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
a = []
with open('a_datamarat.txt', 'r') as f:
    for line in f:
        a.append(float(line))
b = []
with open('b_datamarat.txt', 'r') as f:
    for line in f:
        b.append(float(line))
b_t = []
with open('b_timemarat.txt', 'r') as f:
    for line in f:
        b_t.append(float(line))
a_t =[]
with open('a_timemarat.txt', 'r') as f:
    for line in f:
        a_t.append(float(line))
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
ax = plt.gca()
plt.plot(time, pressure, linewidth=1, color='#52df5b')
print(a)
plt.scatter(a_t, a, s=10, color='red')
plt.scatter(b_t, b, s=10, color='blue')
for i in range(len(a)):
    ax.text(a_t[i], a[i] + 0.05, f"a", fontsize=13)
for i in range(len(b)):
    ax.text(b_t[i], b[i] + 0.05, f"b", fontsize=13)
a_0 = np.array([0 for i in range(len(a))])
low = -3
for i in range(len(a)):
    plt.plot([a_t[i], a_t[i]], [low, a[i]], linestyle='--', linewidth=0.5, color='black')
for i in range(len(b)):
    plt.plot([b_t[i], b_t[i]], [low, b[i]], linestyle='--', linewidth=0.5, color='black')
for i in range(len(a)):
    plt.plot([11.4, a_t[i]], [a[i], a[i]], linestyle='--', linewidth=0.5, color='black')
for i in range(len(b)):
    plt.plot([11.4, b_t[i]], [b[i], b[i]], linestyle='--', linewidth=0.5, color='black')
for i in range(len(a)):
    plt.plot([11.42, 11.42], [b[i], a[i]], linewidth=1, color='black')
    plt.plot([11.42, 11.414], [a[i], a[i] - 0.24], linewidth=1, color='black')
    plt.plot([11.42, 11.426], [a[i], a[i] - 0.24], linewidth=1, color='black')
    plt.plot([11.42, 11.414], [b[i], b[i] + 0.24], linewidth=1, color='black')
    plt.plot([11.42, 11.426], [b[i], b[i] + 0.24], linewidth=1, color='black')
for i in range(len(b)):
    plt.plot([a_t[i] + 0.01, b_t[i] - 0.01], [low + 0.09, low + 0.09], linewidth=1, color='black')
    plt.plot([a_t[i] + 0.01, a_t[i] + 0.03], [low + 0.09, low + 0.15], linewidth=1, color='black')
    plt.plot([a_t[i] + 0.01, a_t[i] + 0.03], [low + 0.09, low+0.03], linewidth=1, color='black')
    plt.plot([b_t[i] - 0.01, b_t[i] - 0.03], [low + 0.09, low + 0.15], linewidth=1, color='black')
    plt.plot([b_t[i] - 0.01, b_t[i] - 0.03], [low + 0.09, low + 0.03], linewidth=1, color='black')
for i in range(len(b)):
    ax.text((a_t[i] + b_t[i])/2, low + 0.12, f"T", horizontalalignment='center', fontsize=13)
for i in range(len(a)):
    ax.text(11.426, (a[i] + b[i]) / 2, f"a-b", verticalalignment='center', fontsize=13)
tick_spacing_x = 0.1
tick_spacing_y = 0.1
ax.grid(which="major", linewidth=0.5)
ax.grid(which="minor", color='lightgrey', linewidth=0.5, linestyle='--')
ax.set_xlabel('Время [c]', fontdict={'fontsize':10.0})
ax.set_ylabel('Давление + const [мм рт. ст.]', fontdict={'fontsize':10.0})
ax.set_title('Артериальное давление \n отдельные колебания волны', fontdict={'fontsize':10.0})
ax.xaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_x))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(tick_spacing_y))
plt.xlim(11.4, 12.6)
plt.ylim(-3, 3)
fig.savefig('graph.png')
plt.show()