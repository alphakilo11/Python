import random, time

anzahl_wuerfe = 1000000
anzahl_serie = 6 # > 1

start = time.thread_time_ns()

muenzwuerfe = []
serien = 0
treffer = 0
serienrekord = 0
for i in range(anzahl_wuerfe):
  muenzwuerfe.append(random.randint(0,1))
for i in range(anzahl_wuerfe - 1):
  if (muenzwuerfe[i] == muenzwuerfe[i + 1]):
    treffer += 1
    if (treffer + 1) > serienrekord:
      serienrekord = (treffer + 1)
    if treffer >= anzahl_serie - 1:
      serien +=1
  else:
    treffer = 0
dauer = time.thread_time_ns() - start
print(f"Anzahl Serien: {serien}, laengste Serie: {serienrekord}. Laufzeit: {dauer} ns")
