def loss_analysis(filepath, variant=True):
  """
  Executes an analysis on data from https://www.oryxspioenkop.com
  Russian losses: https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html
  Ukrainian losses: https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-ukrainian.html
  """
  import re
  searchexpression = r'(T-\d\d)' # Search for T-xx tanks

  with open(filepath) as file:
    data = file.read()

  #find vehicle category
  categories = []
  temp = re.findall(r'([A-z][ A-z]*)( \()', data)
  if temp != None:
    print(len(temp))
    #for i in range(1, len(temp), 2):
    #  print(temp[i])
    #categories.append(temp.group('category'))
  #print(categories)

  data = data.split('\n')
  if variant == True:
    result = []    
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<variant>' + searchexpression + r'.*)(:)', line)
      if temp != None:
        result.append(temp.groupdict())
    return result
  else:
    result = {}
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<model>' + searchexpression + r')', line)
      if temp != None:
        counter = result.get(temp.group('model'), 0)
        result[temp.group('model')] = counter + int(temp.group('number'))
    return result

spam = loss_analysis('/content/test.txt', False)
print(spam)
print(sum(spam.values()) + 180)

import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()