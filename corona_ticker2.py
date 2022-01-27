import random
neue_faelle = (1980, 284, 847, 567, 760, 939, 1038, 240, 117)
bundeslaender = ("Wien", "Vorarlberg", "Tirol", "Steiermark", "Salzburg", "Oberoesterreich", "Niederoesterreich", "Kaernten",  "Burgenland")
faelle_pro_tag = 132697
tick = 3600 * 24 * 7/ faelle_pro_tag
counter = 0
while True:
#  counter += 1
  print("\b" * 20, bundeslaender[random.randint(0, (len(bundeslaender) - 1))])
  time.sleep(tick)
  
