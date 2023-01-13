def read_FFT3_data(filepath):
  import pandas as pd
  df = pd.read_excel(filepath)
  return df

import random # should be imported at top level to speed up dice throws

def dice_throw():
  return random.randint(1,6)

def anti_vehicle_fire(range=4, quality=0, rof=3, heat=False, terrain_saving_throw=0, terrain_saving_throw_modifiers=0, penetration=7, armor=(5, 'A', 3)):
  """
    • Roll to hit—1d6 per ROF of the weapon. To hit requires a 3+ at close
  range, 4+ at effective range and 5+ at long range. Missiles’ to-hit numbers
  are:
  ◦◦ 1st generation missiles with unlimited ammo: 5+; with limited
  ammo: 6.+
  ◦◦ 2nd generation missiles with unlimited ammo: 3+; with limited
  ammo: 4+.
  ◦◦ 3rd generation missiles with unlimited ammo: 2+; with limited
  ammo: 3+.
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
  
  
unit_data = pd.concat([read_FFT3_data('/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/FFT3-Vehicle+Arty+Inf-Data-1950+-v03.xlsx'), read_FFT3_data('/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/FFT3-Vehicle+Arty+Inf-Data-Pre-1950-v03.xlsx')], axis=0)

