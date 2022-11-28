"""https://projecteuler.net/problem=49"""
import math
from timeit import default_timer as timer
def is_prime(number):
  for divisor in range(3, math.ceil(number ** 0.5)):
    if number % divisor == 0:
      return False
  return True

def is_permutation(list_of_numbers):
  if len(list_of_numbers) < 2:
    return False
  strings = []
  for number in list_of_numbers:
    strings.append(''.join(sorted(str(number))))
  if len(set(strings)) > 1:
    return False
  else:
    return True

increase = 3330
third = 1001 + 2 * increase
while third < 10000:
  first = third - increase * 2
  second = third - increase
  if is_prime(first) and is_prime(second) and is_prime(third):
    if is_permutation((first, second, third)) == True:
      print((first, second, third))
  third += 2
