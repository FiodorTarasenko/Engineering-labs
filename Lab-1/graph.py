import matplotlib.pyplot as plt
import numpy as np
data = np.loadtxt('/home/b03-301/Desktop/maratfedornasta/datamaratpokoy.txt')
data2 = np.loadtxt('/home/b03-301/Desktop/maratfedornasta/timepokoymaratalone.txt')
time_start = data2[0]
time_end = data2[1]
data3 = np.linspace(time_start, time_end, len(data))
plt.plot(data3, data)
plt.show()