#https://www.energie-lexikon.info/luftwiderstand.html
Luftwiderstandsbeiwert = 0.27
Querschnittsflaeche = 2.19 #m²
Dichte = 1.225
Geschwindigkeit = 100 / 3.6
def luftwiderstand(Luftwiderstandsbeiwert,Querschnittsflaeche,Dichte,Geschwindigkeit):
  return Luftwiderstandsbeiwert * Querschnittsflaeche * Dichte / 2 * Geschwindigkeit ** 2
def primaerenergie(kraft, geschwindigkeit, wirkungsgrad):
  return kraft * geschwindigkeit / wirkungsgrad
primaerenergie(luftwiderstand(Luftwiderstandsbeiwert,Querschnittsflaeche,Dichte,Geschwindigkeit), Geschwindigkeit, 0.25)
