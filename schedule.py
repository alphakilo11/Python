# Diensteinteilung
workers = ("a", "b", "c", "d", "e", "f", "g")
hours = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
positions = ("low", "low_co", "med", "high", "high_co")

row1 = []
for i in hours:
  row1.append(i)

print(row1)
print(positions[0] + str(hours[0]))
