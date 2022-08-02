"""
Prime numbers checker adapted for multi-threaded execution.
Find prime numbers between first argument and second argument. Check in increments of third argument.
"""

import sys
from timeit import default_timer as timer

def is_prime_number(number):
  """
  returns True if given integer is a prime number.
  Works only with odd number greater than 2
  I crosschecked this function with sympy.isprime() up to 1.5e7 and it is equivalent although it is slower"""
  for divisor in range(3, round(number ** 0.5 + 1), 2):
    if number % divisor == 0:
      return False
  return True

if int(sys.argv[1]) < 3:
    print("ERROR: This program works only with a starting values >= 3.")
    quit()

#debug
#print(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

start = timer()

count = []
for i in range(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
    if is_prime_number(i):
        count.append(i)
#        count += 1

print(timer() - start)
print(len(count), "Warning: 2 is not included in this count.")