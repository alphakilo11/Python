# Gesucht ist die Anzahl der Arten eine natürliche Zahl (x) als Summe aufeinanderfolgender natürlicher Zahlen darstellen zu können
# Der höchste Summand kann größer als x/2 sein (eg: 1 + 2 = 3) Vermutlich nicht größer als math.ceil(x/2).
import math

zu_teilende_zahl = 5
for i in range(math.ceil(zu_teilende_zahl / 2), 0, -1):
  if (2 * i - 1) == zu_teilende_zahl:
    print("yes!")
  if (3 * i - 3) == zu_teilende_zahl:
    print("yes!")
  if (4 * i - 6) == zu_teilende_zahl:
    print("yes!")
  if (5 * i - 10) == zu_teilende_zahl:
    print("yes!")