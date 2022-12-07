import random
import pickle

#create list of random large integers
bar = []
for i in range(10000):
  bar.append(random.randint(0, int(1e18)))

#save them to a file
with open('pickletest.txt', 'wb') as file:
  pickle.dump(bar, file)

#open the file and create a new list from the contents
with open('pickletest.txt', 'rb') as file:
  cocktail = pickle.load(file)
cocktail[-1]
