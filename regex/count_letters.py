# Count letters and visualize them

import re
from matplotlib import pyplot as plt

message = "Ich gehe jeden Tag zur Schule. Dabei nutze ich bei schönem Wetter das Rad, bei Schlechtwetter den Bus."

bar = "abcdefghijklmnopqrstuvwxyz"
ys = []
x = []
for i in bar:
  foo = str(i + "|" + i.upper())
  phoneNumberRegex = re.compile(foo)
  hits = phoneNumberRegex.findall(message)
#  print(i, len(hits))
  ys.append(len(hits))
  x.append(i)

plt.plot(x, ys, '-')
plt.title("Letter count")
plt.show()
