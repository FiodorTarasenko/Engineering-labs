import pandas as pd
from scipy import optimize
import numpy as np
import matplotlib.pyplot as plt
c = 0
n = 0
y = []
with open('data40.txt') as f:
    for line in f:
        s = line
        c += 1
        n += float(s)
    y.append(n / c)
    n = 0
    c = 0
with open('data80.txt') as f:
    for line in f:
        s = line
        c += 1
        n += float(s)
    y.append(n / c)
    n = 0
    c = 0
with open('data120.txt') as f:
    for line in f:
        s = line
        c += 1
        n += float(s)
    y.append(n / c)
    n = 0
    c = 0
with open('data160.txt') as f:
    for line in f:
        s = line
        c += 1
        n += float(s)
    y.append(n / c)
    n = 0
    c = 0
with open('data200.txt') as f:
    for line in f:
        s = line
        c += 1
        n += float(s)
    y.append(n / c)
    n = 0
    c = 0

x = np.linspace(40, 200, 5)

fig, ax = plt.subplots()
coefs = np.polyfit(x, y, 1)
p = np.poly1d(coefs)

print(coefs)

plt.plot(x, p(x), color='navy', linestyle='-', linewidth=1.2)
plt.xlabel("p [мм рт. ст.]")
plt.ylabel("Цифровое значение")
plt.grid(True, color='lightgray', linestyle='--')
ax.set_axisbelow(True)
plt.plot(x, y, 'o', c='black', markersize=5, markeredgecolor='black', markerfacecolor='red', markeredgewidth=1)
title_text = 'График 1: калибровка'
ax.set_title(title_text, wrap=True)
plt.savefig("Калибровка.png", dpi=300)
plt.show()
with open('coefficients.txt', 'w') as f:
    for i in coefs:
        f.write(str(i) + '\n')
