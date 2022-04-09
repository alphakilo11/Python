#p 4
def dreieckszahl(x):
    """Summe der ersten n natuerlichen Zahlen"""
  return int(((x + 1) * x) / 2)

# Gesucht ist die Anzahl der Arten eine natuerliche Zahl (x) als Summe aufeinanderfolgender natuerlicher Zahlen darstellen zu koennen
# Der hoechste Summand kann groeßer als x/2 sein (eg: 1 + 2 = 3) Vermutlich nicht groeßer als math.ceil(x/2).
# IMPROVE optimise speed
import math

zu_teilende_zahl = 111
max_summanden = 10
debug = 0
iterationen = 0
treffer = 0
for i in range(math.ceil(zu_teilende_zahl / 2), 0, -1): # hoechster Summand
  for j in range(2, max_summanden, 1): # Anzahl der Summanden
    iterationen += 1
    if debug == 1:
      print(f"{j} * {i - 1} - {dreieckszahl(j - 1)} = {(j * i - dreieckszahl(j))}")
    if j > (i - 1):
      break
    if (j * i - dreieckszahl(j)) == zu_teilende_zahl:
      treffer += 1
      if debug == 1:
        print("yes!")
print(treffer, " Treffer bei ", iterationen, " Iterationen")