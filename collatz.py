from timeit import default_timer as timer

def collatzer():
    for j in range(1000000):
        i = j
        while i > 1:
            if i % 2 == 0:
                i = i // 2
            else:
                i = (3 * i) + 1

start = timer()
collatzer()
end = timer() - start
print(end)
