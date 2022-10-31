# inspired by Kahnemann, I try to test if humans are faster in finding a negative smily, than a positive smily.
import random
import shelve
from timeit import default_timer as timer
with shelve.open('find_face') as db:
  db['find_angry'] = []
  db['find_happy'] = []

number_of_faces = 3**2
faces_per_line = int(number_of_faces ** (1/2))
the_angry_one = random.randint(0, number_of_faces - 1)
cursor = 0
for i in range(the_angry_one):
  cursor += 1
  print("🙂", end="")
  if cursor >= faces_per_line:
    print()
    cursor = 0
cursor += 1
print("🙁", end="")
if cursor >= faces_per_line:
  print()
  cursor = 0
for i in range(the_angry_one, number_of_faces - 1):
  cursor += 1
  print("🙂", end="")
  if cursor >= faces_per_line:
    print()
    cursor = 0
start_time = timer()
input()
duration = timer() - start_time
print(duration)
with shelve.open('find_face') as db:
  spam = db['find_angry']
  spam.append([duration, number_of_faces])
  db['find_angry'] = spam