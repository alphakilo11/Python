# Wie lange ist ein Augenblick für ... ? https://de.wikipedia.org/wiki/Gegenwart#Gehirnforschung

s_pro_jahr = 31557600
augenblicke_pro_menschenleben = 73.4 * s_pro_jahr / 2.7 # https://de.wikipedia.org/wiki/Lebenserwartung

augenblick = {}
augenblick["Mensch"] = 2.7 # s
augenblick["Graupapagei"] = 50 * s_pro_jahr /  augenblicke_pro_menschenleben
augenblick["Universum"] = alter_des_universum_in_s / augenblicke_pro_menschenleben # aktuelles Alter
augenblick["Erde"] = 4.6e9 * s_pro_jahr /  augenblicke_pro_menschenleben # aktuelles Alter
augenblick["Sonne"] = 12.5e9 * s_pro_jahr /  augenblicke_pro_menschenleben # Lebenserwartung


for i in augenblick.keys():
  print (i, augenblick[i] / s_pro_jahr, 'Jahre')
