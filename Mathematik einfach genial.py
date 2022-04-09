# Gesucht ist die Anzahl der Arten eine natuerliche Zahl (x) als Summe aufeinanderfolgender natuerlicher Zahlen darstellen zu koennen
# Der hoechste Summand kann groeßer als x/2 sein (eg: 1 + 2 = 3) Vermutlich nicht groeßer als math.ceil(x/2).
import math

zu_teilende_zahl = 18
iterationen = 0
for i in range(math.ceil(zu_teilende_zahl / 2), 0, -1): # hoechster Summand
  for j in range(2, 6, 1): # Anzahl der Summanden
    iterationen += 1
    print(f"{j} * {i} - {dreieckszahl(j)} = {(j * i - dreieckszahl(j))}")
    if (j * i - dreieckszahl(j)) == zu_teilende_zahl:
      print("yes!")
print(iterationen)