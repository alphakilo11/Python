def read_FFT3_data(filepath):
  import pandas as pd
  df = pd.read_excel(filepath)
  return df

read_FFT3_data('/content/drive/MyDrive/Brettspiele&Co/Wargames/Züge/FFT3/Unit Data/Pre 1950s/WW1 German and British Stats.xlsx')[11:]

