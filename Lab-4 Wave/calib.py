import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
data_x = []
for i in range(40, 121, 20):
    data = np.loadtxt(rf"C:\Users\marat\Desktop\wave\{i}.txt")
    print(data)
    data_x.append(np.mean(data))
data_x = np.array(data_x)
data_y = np.array([i for i in range(40, 121, 20)])
new_x = np.arange(0, 160, 0.0001)
deg = 2
k = np.polyfit(data_x, data_y, deg)
f = np.poly1d(k)
plt.ylim(0, 130)
plt.plot(new_x, f(new_x))
plt.scatter(data_x, data_y)
k_str = [str(round(i, 4)) for i in k]
k_str.append(str(deg))
print(k_str)
with open(r"C:\Users\marat\Desktop\wave\k.txt", 'w') as f:
    f.write("\n".join(k_str))
plt.show()
