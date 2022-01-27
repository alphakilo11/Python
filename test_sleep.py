import time
start = time.time()
repeats = 100000
sleep_time = 0.00001
for i in range(repeats):
  time.sleep(sleep_time)
completion_time = time.time() - start
print("fertig in: ", completion_time ," s, Abweichung vom Erwartungswert:", (completion_time- repeats * sleep_time) / completion_time * 100," %")
