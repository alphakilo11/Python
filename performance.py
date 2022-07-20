import time
import numpy as np
start = time.perf_counter_ns()
foo = np.arange(int(1.5e7))
print(time.perf_counter_ns() - start)
