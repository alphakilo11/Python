import imp
import numpy as np
from timeit import default_timer as timer

start = timer()
for i in range(10):
  foo = np.arange(5607249)
  del foo
print(timer() - start)