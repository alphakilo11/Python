import math
def lorenzfaktor(geschwindigkeit):
  return 1 / math.sqrt(1 - (geschwindigkeit / scipy.constants.c) ** 2)

"""Vergangene Zeit im bewegten System berechnen"""
zeit_ruhe = 365*24*3600
geschwindigkeit = scipy.constants.c * 2.5551009692178446e-05
print("Delta Zeit in Bewegnung: ", zeit_ruhe / lorenzfaktor(geschwindigkeit) - zeit_ruhe)

"""nötige Geschwindigkeit für bestimmte Zeiten berechnen"""
zeit_ruhe = 12
zeit_bewegt = 4
print(" Lichtgeschwindigkeit: ", math.sqrt(1 - (1/(zeit_ruhe / zeit_bewegt))**2))
