# this gets my Windows 11 Computer to 100% load. But Im not sure what it actually does and how to properly use it (for example to calculate Collatz)
# After some time at 100% the CPU load on my 12600K drops step by step...
# ... this leads me to the assumption, that the performance cores finish their job quicker and start to idle
# MBP M1 loads to almost 100% and stays there until the job is done
# https://docs.python.org/3.8/library/multiprocessing.html#module-multiprocessing

from multiprocessing import Pool, cpu_count
import multiprocessing
from timeit import default_timer as timer

poolNumber = cpu_count() # CPUs?
otherNumber = poolNumber * 2 # Threads?
list_for_map = [1] * otherNumber

def f(x):
    for i in range(x * 1000000):
        n = i
        while n > 1:
            n = n // 2 if n % 2 == 0 else n * 3 + 1
    print("Done!")

start = timer()

if __name__ == '__main__':
    with Pool(poolNumber) as p:
        p.map(f, list_for_map)

end = timer() - start
print(end)        
