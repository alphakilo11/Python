from timeit import default_timer as timer
import numpy as np

# create a self adjusting program that adjust itself to execute a given function as often as possible in a given timeframe (not missing it by a given margin)
#ENHANCE if the function takes ever longer to execute it's not optimal (and might even lead to missing the timeframe entirely) to start measuring with the fastest values

def f(x):
  sum = 1
  for i in range(1, x):
    sum *= i
  return sum

def calc_req_loops(req_precision, x):
  prec_timer = timer()
  f(x)
  prec_timer = timer() - prec_timer
  return int(required_precision / prec_timer)

required_time = 10
required_precision = required_time * 0.0005 # s off given time

debug = []
start = timer()
try:
  count = 0
  cursor = 0
  while timer() - start < required_time:
    number_of_loops = calc_req_loops(required_precision, cursor)
    number_of_loops = number_of_loops if number_of_loops > 0 else 1
    debug.append(number_of_loops)
    for i in range(number_of_loops):
      count = f(cursor)
      cursor += 1
finally:
  print(timer() - start)
  print(count)
  print(cursor)
  print(debug)
