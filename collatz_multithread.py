import time
from threading import Thread

number_of_threads = 18

def collatz(threadname, ende):
    for i in range(1, ende):
        while i != 1:
            if i % 2 == 0:
                i = i / 2
            else:
                i = 3 * i + 1
    print("Thread number", threadname, "done.")

start = time.time()

try:
    threads = []
    for i in range(number_of_threads):
        t = Thread(target=collatz, args=(i, 100000))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

except:
    print("Error")

print(time.time() - start)