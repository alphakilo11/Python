from matplotlib import pyplot as plt
import time

with open("temp_log2.txt") as file:
    data = file.read()
cleanup_list = [" ", "[", "'"]
for char in cleanup_list:
    data = data.replace(char, "")
data = data.split("],")

x_values = []
y_values = []
for i in range(1, len(data) - 1):
    step = data[i].split(",")
    x_values.append(int(step[0]))
    print(time.localtime(int(step[0]))[3],":", time.localtime(int(step[0]))[4], int(step[0]))
    y_values.append(int(step[1]))

plt.plot(x_values, y_values, '-')

plt.title("Temperature Histogramm")
plt.show()