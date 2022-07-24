# https://projecteuler.net/problem=27
from timeit import default_timer as timer
import numpy as np

def divisors(number):
  """returns the proper divisors of a positive integer"""
  divisors = [1]
  for i in range(2, round(number / 2) + 1):
    if number % i == 0:
      divisors.append(i)
  return divisors

def is_abundant(number):
  """returns True if a number is abundant. (https://projecteuler.net/problem=23)"""
  if np.sum(divisors(number)) > number:
    return True
  else:
    return False

def pe_23(candidate, numbers):
  """returns True if a positive integer can be written as the sum of two out of a list of numbers."""
  for j in numbers:
    if j >= candidate:
      break
    for k in numbers:
      if j + k > candidate or k >= candidate:
        break
      if j + k == candidate:
        return True
  return False

def digit_sum(number):
  """returns the digit sum of a number"""
  sum = 0
  for i in str(number):
    sum += int(i)
  return sum

def faculty(x):
  """returns the faculty of a number"""
  result = x
  for i in range(1, x):
    result *= i
  return result

def dreieckszahlen(anzahl):
  """returns the given number of triangle numbers"""
  zahlen = []
  for i in range(1, anzahl):
    zahlen.append((i * (i + 1)) / 2)
  return zahlen

def primzahlengenerator(beginn, ende):
  """returns prime number between beginn and ende"""
  primzahlen = []
  if beginn < 3:
    primzahlen.append(2)
    beginn = 3
  for i in range(beginn, ende):
    abgelehnt = False
    for j in range(2, (round(i ** 0.5) + 1)):
      if i % j == 0:
        abgelehnt = True
    if abgelehnt == False:
      primzahlen.append(i)
    i += 2
  return primzahlen


def collatz(number):
  """returns the number of terms in a collatz sequence"""
  candidate = number
  counter = 1
  while candidate != 1:
    if candidate % 2 == 0:
      candidate = candidate // 2
    else:
      candidate = candidate * 3 + 1
    counter += 1
#    print(candidate)
  return counter

def fibonacci(one, two):
    return one + two

def check_reciprocal_cycle(dividend, divisor):
  """Returns the number of digits of a fractions recurring cycle in it's decimal fraction part (0 if no recurring cycle was found)"""
  fraction_part = []
  count = -1
  while True:
    count += 1
    temp = dividend % divisor
    if temp in fraction_part:
      return count
    if temp == 0:
      return 0
    fraction_part.append(temp)
    dividend = temp * 10
    while dividend < divisor:
      dividend *= 10

def is_prime_number(number):
  if number % 2 == 0 or number <= 1:
    return False
  for divisor in range(3, round(number ** 0.5)):
    if number % divisor == 0:
      return False
  return True

start = timer()

try:
  winner = [0,0,0]
  for co_1 in range(-999, 1000):
    for co_2 in range(-1000, 1001):
      n = 0
      while True:
        if is_prime_number(n ** 2 + co_1 * n + co_2):
          n += 1
        else:
          if n > winner[0]:
            winner = [n, co_1, co_2]
          break
finally:
  print(timer() - start)
  print(winner)
  del start, co_1, co_2, n