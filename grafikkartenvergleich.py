# Grafikkartenvergleich 04apr2022
grafikkarten = ["RTX 3090", "RTX 3080 Ti", "RTX 3080", "RX 6900-XT", "RTX 3070 Ti", "RX 6800-XT", "RTX 3070"]
userbenchmark = [234, 234, 208, 196, 167, 163, 154]
geizhals_eu = [1849, 1299, 998, 1099, 763, 927, 699]

for i in range(len(grafikkarten)):
  print(round(userbenchmark[i] / geizhals_eu[i] * 100, 2), "\t", grafikkarten[i], "\t", userbenchmark[i], "\t€", f"{geizhals_eu[i]:4}")