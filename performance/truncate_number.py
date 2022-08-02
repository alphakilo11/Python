# slow
def truncate_integer_left(number):
  power = len(str(number)) - 1
  return number - (number // 10 ** power * 10 ** power)

# fast
def truncate_integer_left(number):
  return int(str(number)[1:])
