"""Corona Ticker"""
faelle_pro_tag = 132697
tick = 3600 * 24 * 7/ faelle_pro_tag
counter = 0
while True:
  counter += 1
  print("\b" * 15, counter)
  time.sleep(tick)
  
