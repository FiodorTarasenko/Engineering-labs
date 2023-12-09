import numpy as np
import matplotlib.pyplot as plt

x = [140, 295]
x1 = [0, 140, 295, 430]
y = [436, 577]

coeffs = np.polyfit(x, y, 1)
p = np.poly1d(coeffs)

fig, ax = plt.subplots()
plt.plot(x1, p(x1), c='royalblue', linestyle='-', linewidth=1.8)
csfont = {'fontname': 'Arial', 'size': 16}
hfont = {'fontname': 'Arial', 'size': 19}
plt.xlabel("Относительный номер пикселя", **csfont)
plt.ylabel("Длина волны", **csfont)
plt.minorticks_off()
plt.grid(True, which='major', color='papayawhip', linestyle='--')
ax.set_axisbelow(True)
# plt.scatter(x, y, s=50, marker='x', c='mediumseagreen', linewidths=1)
title_text = 'Калибровочная прямая'
ax.set_title(title_text, wrap=True, **hfont)

ax.set_xlim(0, 430)

plt.savefig("Calib.png", dpi=300)
plt.show()
with open('coefficients.txt', 'w') as f:
    for i in coeffs:
        f.write(str(i) + '\n')