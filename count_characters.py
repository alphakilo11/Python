# this is also very handy to check for Umlauts

text = '# Berechnung bedrohter Flaeche '
count = {}
for i in text:
  count.setdefault(i, 0)
  count[i] = count[i] + 1
count
