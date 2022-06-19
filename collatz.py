import time
start = time.time()
for i in range(3,1000000):
  #print(i, end=" ")
  while i != 1:
    if i % 2 == 0:
      i = i / 2
    else:
      i = 3 * i + 1
    #print(i, end=" ")
  #print("")
print(time.time() - start)