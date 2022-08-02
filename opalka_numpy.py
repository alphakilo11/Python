from os import times
import numpy as np
from timeit import default_timer as timer
from matplotlib import pyplot as plt

attempts = 100

time_list = []
for i in range(attempts):
  start = timer()
  foo = np.arange(5607249)
  time_list.append(timer() - start)
  del foo
print(f"Best time out of {attempts} attempts: {min(time_list)}")
ys = time_list
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
#plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()
del time_list, attempts, x, ys

