# 3e9 takes 24 GB of RAM (64-bit per entry)
# 1e9 takes  4 GB of RAM (32-bit per entry)
# 0.9541288999607787 Core i5-12600K numpy.arange(1e9)

from timeit import default_timer as timer
import numpy

start_value = int(1e9)

start_time = timer()
foo = numpy.arange(start_value)
print(timer() - start_time)
input()
del foo