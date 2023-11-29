import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import matplotlib.ticker as ticker
import math
c = []
with open(r'C:\Users\marat\Desktop\wave\c.txt', 'r') as f:
    for line in f:
        c.append(float(line))
c = np.array(c)
c = np.log(c)
h = []
with open(r'C:\Users\marat\Desktop\wave\c.txt', 'r') as f:
    for line in f:
        h.append(float(line))
h = np.array(h)
h = np.log(h)

#approx
coeffs = np.polyfit(h, c, 1)
p = np.poly1d(coeffs)
plt.plot(h, p(h), color='red', linestyle='-', linewidth=1)
print(coeffs[0])               #should be 0.5
print(np.exp(2 * coeffs[1]))   # value of g

data_x = np.arange(-5, np.max(h))
g = 0.5*(math.log(9.81))
data_y = 0.5*data_x + g
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
ax.plot(data_x, data_y)
ax.scatter(h, c)
plt.show()
