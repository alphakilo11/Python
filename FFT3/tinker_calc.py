def read_FFT3_data(filepath, sheet_name=0):
  """
  Requires pandas as pd
  """
  df = pd.read_excel(filepath,sheet_name=sheet_name)
  return df

import random # should be imported at top level to speed up dice throws
import pandas as pd

def dice_throw():
  return random.randint(1,6)

to_hit_values = {'range': {'close': 3, 'effective': 4, 'long': 5}, 'missiles': {'1st_unlimited': 5, '1st_limited': 6, '2nd_unlimited': 3, '2nd_limited': 4, '3rd_unlimited': 2, '3rd_limited': 3}}
#quality_modifiers = {'poor':}

def anti_vehicle_fire(distance=4, quality=0, rof=3, heat=False, terrain_saving_throw=0, terrain_saving_throw_modifiers=0, penetration=7, armor=(5, 'A', 3)):
  """
  Phase 1
    Implement rules iot calculate battles between armored vehicles without any modifiers, missiles or heat or he ammo
  Phase 2
  • Add quality modifiers and other applicable modifiers to all to-hit rolls.
  • An armor value modifier is used when attacked by h-class weapons.
  • If the target is in some kinds of terrain, or behind some types of obstacles,
  it may get a saving throw on 1d6 for each hit you score.
  • For each hit that isn’t saved, roll the number of dice equal to the weapon’s
  Pen minus the target’s Armor.
  • If any die is a “6”, the target is destroyed. If any die is a 4 or 5, the target
  must make a quality check. One anti-vehicle fire quality check maximum
  per phase.
  Natural 1 always misses, 6 always hits
  """
  rolls = []
  for i in range(rof):
    rolls.append(dice_throw())
  threshold = distance + quality
  hits = 0
  for die in rolls:
    if die == 6 or die >= threshold:
      hits += 1
      continue
    else:
      continue
  #print(hits, 'hits.')
  # terrain saving throws
  # ...

  # penetration rolls
  # ENHANCE optimize this part for performance
  if hits > 0:
    penetration_rolls = []
    penetration_difference = penetration - int(armor[0])
    for hit in range(hits * penetration_difference):
      penetration_rolls.append(dice_throw())

    return penetration_rolls
  
  return hits # returns 0 if no hits were scored

def load_unit_data(filepath='/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/FFT3-Vehicle+Arty+Inf-Data-Pre-1950-v03.xlsx'):   
  """ 
  Load unit data and concatenate it to a single Pandas Dataframe
  Use spam[spam["Name"] == "R35"].squeeze()["Period"] to fetch specific values 
  type(spam[spam["Name"] == "R35"].squeeze()["Period"]) == type('') will check if it returned a single value (mulitple hits are possible, as Name is non-unique
  """

  from google.colab import drive
  drive.mount('/content/drive')

  pre50_vehicles = read_FFT3_data('/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/FFT3-Vehicle+Arty+Inf-Data-Pre-1950-v03.xlsx', sheet_name=2)
  pre50_artillery = read_FFT3_data('/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/FFT3-Vehicle+Arty+Inf-Data-Pre-1950-v03.xlsx', sheet_name=3)
  #pre50_infantry
  #vehicles  
  #artillery
  #infantry
  unit_data = pd.concat([pre50_vehicles, pre50_artillery], axis=0)
  return unit_data

def attack(unit_database, attacker='Pz. IVD', defender='T-34/76A m.1940', debug=False):
  attacker_values = unit_database[unit_database["Name"] == attacker].squeeze()
  defender_values = unit_database[unit_database['Name'] == defender].squeeze()
  # check if multiple entries are returned
  if type(attacker_values['Period']) != type(''):
    print('ERROR: attacker is not unique, aborting.')
    return
# !!! CONTINUE here!!!!

  result = anti_vehicle_fire(distance=4, quality=0, rof=int(attacker_values['Gun ROF']), heat=False, terrain_saving_throw=0, \
  terrain_saving_throw_modifiers=0, penetration=int(attacker_values['Gun Pen']), armor=defender_values['Armor'].split(' '))
  return result

unit_data = load_unit_data()
attack(unit_data)