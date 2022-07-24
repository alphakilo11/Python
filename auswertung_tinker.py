import json
from matplotlib import pyplot as plt

with open("temp_log1.txt", "r") as file:
    foo = file.read()
foo = json.loads(foo)
print(foo["temperatur"][-5]["time_epoch"])


ys = []
for i in range(len(foo["temperatur"])):
    ys.append(foo["temperatur"][i]["temperature"])
x = []
for i in range(len(foo["temperatur"])):
    x.append(foo["temperatur"][i]["time_epoch"])
print(len(ys), len(x), ys[:5], x[:5])

plt.plot(x, ys, '-')

plt.title("Temperature Histogramm")
plt.show()