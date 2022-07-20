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
