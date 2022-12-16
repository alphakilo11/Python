import sympy
from timeit import default_timer as timer

range_lower = 3
range_upper = int(1e6)
# sympy.primerange
start_time = timer()
length = len(list(sympy.primerange(range_lower, range_upper)))
print("sympy.primerange took:", timer() - start_time, "s and found", length)
# sympy.isprime
start_time = timer()
results = []
for i in range(range_lower, range_upper, 2):
  if sympy.isprime(i):
    results.append(i)
length = len(results)
print("sympy.isprime took:", timer() - start_time, "s and found", length)
del results
# homebrew
def is_prime(candidate):
  for divisor in range(3, round(candidate ** 0.5) + 1, 2):
    if candidate % divisor == 0:
      return False
  return True
start_time = timer()
results = []
for i in range(range_lower, range_upper, 2):
  if is_prime(i):
    results.append(i)
length = len(results)
del results
print("homebrew took:", timer() - start_time, "s and found", length)

def prime_time(candidate, number):
  from timeit import default_timer as timer
  import matplotlib.pyplot as plt

  step = 10000
  results = []
  milestones = []
  i = 33333333333333333333
  counter = len(results)

  start_time = timer()
  step_time = start_time
  while (timer() - start_time) <= number:
    if candidate(i):
      results.append(i)
    i += 2
    counter += 1
    if counter % step == 0:
      temp_time = timer()
      milestones.append(temp_time - step_time)
      step_time = temp_time

  duration = timer() - start_time

  # Data for plotting
  s = milestones
  t = range(0, len(milestones))

  fig, ax = plt.subplots()
  ax.plot(t, s)

  ax.set(xlabel='calculated primes', ylabel='time (s)',
        title=str(candidate))
  ax.grid()

  fig.savefig("test.png")
  plt.show()

  return [duration, len(results), len(milestones)]

  print(prime_time(is_prime, 1))

  print(prime_time(sympy.isprime, 1))
