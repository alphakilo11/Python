import time
start = time.time()
def collatz(ende):
    for i in range(1, ende):
        while i != 1:
            if i % 2 == 0:
                i = int(i * 0.5) #int saves ca. 10% time
            else:
                i = 3 * i + 1

collatz(1000000)
print(time.time() - start)