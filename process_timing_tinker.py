import time

start = time.thread_time_ns()
for i in range(5607249):
    continue
print(f"Elapsed thread time: {time.thread_time_ns() - start} ns")