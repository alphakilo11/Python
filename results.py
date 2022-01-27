"""
BUG Precision ist in diesem Fall irreführend; werden lauter 7er geschossen, so wäre die Präzision 0, aber dies entspricht nicht der Realität.
Klassen für verschiedene Wettbewerbsmode verwenden?
tag results, sodass ein Programm weiß welche Werte die Ergebnisse sind?
(Datum YYYYMMDD, Wettbewerbs-ID GUID, Schützen-ID GUID, Scores)
"""

import statistics

results = ((20220127, 7, 7, 7, 7, 7, 7, 7),
           (20220127, 10, 10, 9, 8, 9, 4, 10),
           (20220127, 10, 10, 9, 8, 5, 10, 10),
           (20220127, 10, 10, 9, 8, 7, 10, 10),
           (20220127, 10, 10, 9, 8, 9, 10, 10))

summe = 0
for i in range(1, len(results[0])):
  summe += results[0][i]
print(f"Gesamtpunkte: {summe}, Trueness: {((len(results[0]) - 1) * 10) - summe} Precision: {statistics.pstdev(results[0][1:])}")
