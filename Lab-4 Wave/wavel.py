import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import matplotlib.ticker as ticker
k = []
l = 1.39
with open(r"C:\Users\marat\Desktop\wave\k.txt", 'r') as f:
    for line in f:
        k.append(float(line))
deg = int(k[-1])
k = k[:len(k)-1]
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
data = np.loadtxt(r'C:\Users\marat\Desktop\wave\exs100.txt')
y = np.array([data[i] for i in range(len(data) - 1)])
y_0 = np.array([float(0) for i in range(len(y))])
k = [k[i] for i in range(len(k)-1, -1, -1)]
print(k)
for i in range(deg, -1, -1):
    y_0 += k[i] * (y**i)
    print(y_0)
x_0 = np.linspace(0, data[-1], len(y_0))
arr = y_0
arr1 = x_0
maxima_indices = argrelextrema(arr, np.greater, order=1)
maxima_values = arr[maxima_indices]
print(len(maxima_values))
for i in range(len(maxima_values)-2):
    if (maxima_values[i] - maxima_values[i+2]) > 10:
        a = maxima_values[i+1]
        break
ind = np.where(arr == a)
print(a)
print('ind', ind[0][0])
print(ind)
o = len(ind[0])-6
data_x = arr1[0:ind[0][o]]
data_x_0 = arr1[ind[0][-1]:ind[0][-1] + 20]
data_y = arr[0:ind[0][o]]
data_y_0 = arr[ind[0][-1]:ind[0][-1] + 20]
coeff = np.polyfit(data_x, data_y, 1)
f = np.poly1d(coeff)
coeff_0 = np.polyfit(data_x_0, data_y_0, 1)
f_0 = np.poly1d(coeff_0)
t = (coeff_0[1]-coeff[1])/(coeff[0] - coeff_0[0])
c = 2*l/t
diff = np.abs(arr1 - t)
index = np.argmin(diff)
x_l = np.arange(0, t+0.5, 0.0001)
y_l = coeff[0] * x_l + coeff[1]
x_1 = np.arange(t-0.5, t+3, 0.0001)
y_1 = coeff_0[0] * x_1 + coeff_0[1]
ax.plot(x_l, y_l, linewidth=0.5, color='red')
ax.plot(x_1, y_1, linewidth=0.5, color='red')
ax.plot(x_0, y_0, linewidth=0.5, color='blue')
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.tick_params(which='major', direction='out')
plt.tick_params(which='minor', direction='out')
plt.grid(which="major", color='black', linewidth=0.2)
plt.grid(which="minor", color='grey', linewidth=0.1)
fig.savefig('graph.png')
print(c)
plt.show()
with open(r"C:\Users\marat\Desktop\wave\c.txt", "a+") as file_object:
    file_object.seek(0)
    data = file_object.read(100)
    if len(data) > 0:
        file_object.write("\n")
    file_object.write(str(round(c, 3)))