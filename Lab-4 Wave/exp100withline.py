import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import matplotlib.ticker as ticker
k = []
l = 1.39
with open(r"C:\Users\marat\Desktop\wave\exp100.txt", 'r') as f:
    for line in f:
        k.append(float(line))
dac = np.array(k[0:len(k)-1])
t = np.linspace(0, k[-1], len(dac))
b = (np.min(dac) + np.max(dac))/2
y = 2*b - dac
arr = y
arr1 = t
#print(ind[0][1])
x = t[:26]
x1 = t[:26 + 50]
#print(x)
y1 = arr[:26]
#print(y1)
coeff = np.polyfit(x, y1, 1)
f = np.poly1d(coeff)
x2 = t[35:67]
x21 = t[25:150]
y2 = arr[35:67]
coeff1 = np.polyfit(x2, y2, 1)
f1 = np.poly1d(coeff1)
x_s = (coeff1[1] - coeff[1])/(coeff[0] - coeff1[0])
print(x_s)
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
ax.scatter(x_s, f(x_s), s=3, color='red')
plt.plot(x21, f1(x21), linewidth=0.8)
plt.plot(x1, f(x1), linewidth=0.8)
plt.plot(t, y, color='blue', linewidth=1)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.tick_params(which='major', direction='out')
plt.tick_params(which='minor', direction='out')
plt.grid(which="major", color='black', linewidth=0.2)
plt.grid(which="minor", color='grey', linewidth=0.1)
plt.xlim(0, 4)
plt.ylim(180, 230)
plt.xlabel('Время [c]')
plt.ylabel('АЦП')
fig.savefig(r"C:\Users\marat\Desktop\wave\exp100withline.png")
plt.show()