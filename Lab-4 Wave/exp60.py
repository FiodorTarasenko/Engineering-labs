import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
k = []
l = 1.39
with open(r"C:\Users\marat\Desktop\wave\exp60.txt", 'r') as f:
    for line in f:
        k.append(float(line))
dac = np.array(k[0:len(k)-1])
t = np.linspace(0, k[-1], len(dac))
b = (np.min(dac) + np.max(dac))/2
y = 2*b - dac
fig, ax = plt.subplots(figsize=(8.25, 5.85), dpi=200)
ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(10))
ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(10))
plt.tick_params(which='major', direction='out')
plt.tick_params(which='minor', direction='out')
plt.grid(which="major", color='black', linewidth=0.2)
plt.grid(which="minor", color='grey', linewidth=0.1)
plt.xlabel('Время [c]')
plt.ylabel('АЦП')
plt.xlim(0, 16)
plt.plot(t, y)
fig.savefig(r"C:\Users\marat\Desktop\wave\exp60.png")
plt.show()