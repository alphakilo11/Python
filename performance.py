from time import perf_counter_ns as timer
import numpy as np

start = timer()
foo = np.arange(int(1.5e7))
print(timer() - start)
del start, foo

# file write performance
import sys
np.set_printoptions(threshold=sys.maxsize)
foo = np.arange(int(1e5))
start = timer()
with open("AK_test_20220720_1.txt", "w") as file:
  file.write(str(foo))
print(timer() - start)
del foo, start
np.set_printoptions(threshold=None)

# isinstance performance
from timeit import default_timer as timer
import random

liste_der_antworten = []
or_times =[]
instance_times = []
for i in range(100):
  for i in range(10000):
    liste_der_antworten.append(random.choice([5, (3,5)]))

  start = timer()
  for i in liste_der_antworten:
    type(i) == list or type(i) == tuple
  or_times.append(timer() - start)

  start = timer()
  for i in liste_der_antworten:
    isinstance(i, (list, tuple))
  instance_times.append(timer() - start)

import statistics
print(statistics.mean(or_times))
print(statistics.mean(instance_times))
