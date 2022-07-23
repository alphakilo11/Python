#  sum the words of a string by word-length and visualize
#BUG if the string starts with a word it is not counted. (workaround: insert blank space at the beginning)
#BUG a word with any character (eg ") in front or behind will not be counted.

import re
from matplotlib import pyplot as plt
message = "I as the earl major. I as the earl major."
start_time = timer()
bar = range(1, 11)
ys = []
x = []
for i in bar:
  foo = str(" \w{" + str(i) + "} ")
  phoneNumberRegex = re.compile(foo)
  hits = phoneNumberRegex.findall(message)
#  print(i, len(hits))
  ys.append(len(hits))
  x.append(i)
print(timer() - start_time)
plt.plot(x, ys, '-')
plt.title("Words by number of characters")
plt.show()
