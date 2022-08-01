# faster (0.05447242999980517 s)
start_value = 0

start = timer()

try:
  for i in range(start_value, start_value + int(1e6)):
    pass
finally:
  print(timer() - start)
  del start, i


# slower (1.3546416989997851 s)
start_value = 0
end_value = 0 + + int(1e7)
start = timer()

try:
  while start_value < end_value:
    start_value += 1
finally:
  print(timer() - start)
  del start, start_value, end_value
