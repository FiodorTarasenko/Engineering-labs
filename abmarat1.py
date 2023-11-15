import numpy as np
a = []
with open('a_datamarat.txt', 'r') as f:
    for line in f:
        a.append(float(line))
a = np.array(a)
b = []
with open('b_datamarat.txt', 'r') as f:
    for line in f:
        b.append(float(line))
b = np.array(b)
a_b = a - b
ave_a_b = np.mean(a_b)
b_t = []
with open('b_timemarat.txt', 'r') as f:
    for line in f:
        b_t.append(float(line))
b_t = np.array(b_t)
a_t =[]
with open('a_timemarat.txt', 'r') as f:
    for line in f:
        a_t.append(float(line))
a_t = np.array(a_t)
b_t_a_t = b_t - a_t
ave_b_t_a_t = np.mean(b_t_a_t)
value = ave_a_b/ave_b_t_a_t
print(value)
value_str = str(value)
ave_a_b_str = str(ave_a_b)
ave_b_t_a_t_str = str(ave_b_t_a_t)
h = 1.88
speed = h/ave_b_t_a_t
speed = str(speed)
with open('valuesmarat.txt', 'w') as f:
    f.write(f" a - b = {ave_a_b_str} mm pt. ct.\n delta T = {ave_b_t_a_t_str} c \n (a-b)/T = {value_str} m/s\n wave speed = {speed} m/s")