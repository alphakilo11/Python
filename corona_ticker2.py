import random
import time
neue_faelle = (8180, 1142, 2517, 4771, 1846, 6148, 8686, 2222, 1451)
bundeslaender = ("Wien", "Vorarlberg", "Tirol", "Steiermark", "Salzburg", "Oberoesterreich", "Niederoesterreich", "Kaernten",  "Burgenland")
tick = 1 / (sum(neue_faelle) / 7 /24 / 3600)
counter = 0
while True:
  print(random.choices(list(bundeslaender), neue_faelle, k=1), "\a")
  time.sleep(tick)
  #print("\b" * 20, end="") #nothing is ever shown...
  
