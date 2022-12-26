import numpy as np
def opalka():
  list(range(5607249))

def ak_timer(code, repetitions):
  from timeit import default_timer as timer
  import matplotlib.pyplot as plt

  times = []
  for i in range(repetitions):
    start_time = timer()
    code()
    times.append(timer() - start_time)
  # plot
  x = range(len(times))
  y = times
  fig, ax = plt.subplots()
  ax.plot(x, y)
  plt.show()
  return times
  
  print(min(ak_timer(opalka, 100)))
