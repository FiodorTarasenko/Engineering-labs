import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import matplotlib.ticker as ticker
import math
c = []
with open(r'C:\Users\marat\Desktop\wave\cnew.txt', 'r') as f:
    for line in f:
        c.append(float(line))
c = np.array(c)
c = np.log(c)
h = []
with open(r'C:\Users\marat\Desktop\wave\h.txt', 'r') as f:
    for line in f:
        h.append(float(line))
h = np.array(h)
h = np.log(h)

#approx
coeffs = np.polyfit(h, c, 1)
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
p = np.poly1d(coeffs)
h1 = np.append(h, -4)
h1 = np.append(h1, 0)
plt.xlim(-4, 0)
plt.plot(h1, p(h1), color='red', linestyle='-', linewidth=1)
print(coeffs[0])               #should be 0.5
print(coeffs[1])   # value of g
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.tick_params(which='major', direction='out')
plt.tick_params(which='minor', direction='out')
plt.grid(which="major", color='black', linewidth=0.2)
plt.grid(which="minor", color='grey', linewidth=0.1)
plt.xlabel('ln(h)')
plt.ylabel('ln(c)')
data_x = np.arange(-5, np.max(h))
g = 0.5*(math.log(9.81))
data_y = 0.5*data_x + g
ax.scatter(h, c)
print(math.exp(coeffs[1]*2))
fig.savefig(r"C:\Users\marat\Desktop\wave\log.png")
plt.show()
