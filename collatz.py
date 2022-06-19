import time
start = time.time()
def collatz(ende):
    for i in range(1, ende):
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = 3 * i + 1

collatz(int(1e5))
print(time.time() - start)