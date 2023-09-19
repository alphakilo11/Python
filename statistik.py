""" This Module is based on the book "Fit fürs Studium Statistik" by Benno Grabinger, 2. korrigierte Auflage 2021 """
def relative_haeufigkeit(absolute_haeufigkeit, grundgesamtheit):
    return absolute_haeufigkeit / grundgesamtheit

def haeufigkeitsdichte(relative_haeufigkeit, klassenbreite):
    """S 47 Säulenhöhe in einem Histogramm."""
    return relative_haeufigkeit / klassenbreite

def klassenmitte(untergrenze, obergrenze):
    """S 50"""
    return (untergrenze + obergrenze) / 2

# Kapitel 4 Lagemaßzahlen
def arithmetisches_mittel(zahlen):
    """Falls ein dict als parameter verwendet wird, geht die Funktion von einer Gewichtung aus. Das Format wird mit {wert:gewicht} angenommen."""
    sum = 0
    if type(zahlen) == type({}):
        """S 88"""
        gesamtgewicht = 0
        for wert, gewicht in zahlen.items():
            sum += gewicht * wert
            gesamtgewicht += gewicht
        return sum / gesamtgewicht
        
    else:
        """S 82"""
        for number in zahlen:
            sum += number
        return sum / len(zahlen)
    
def median(liste_quantitativer_merkmalsauspraegungen):
    """S 94"""
    geordnete_liste = sorted(liste_quantitativer_merkmalsauspraegungen)
    if len(geordnete_liste) % 2 != 0:
        return geordnete_liste[(len(geordnete_liste) + 1) // 2 - 1]
    else:
        return (geordnete_liste[len(geordnete_liste) // 2 - 1] + geordnete_liste[(len(geordnete_liste)) // 2]) / 2

def p_quantil(liste_quantitativer_merkmalsauspraegungen, p):
    """S 97"""
    entscheidungswert = len(liste_quantitativer_merkmalsauspraegungen) * p
    geordnete_liste = sorted(liste_quantitativer_merkmalsauspraegungen)
    if entscheidungswert % 1 != 0:
        import math
        return geordnete_liste[math.floor(entscheidungswert)]
    else:
        return (geordnete_liste[int(entscheidungswert) - 1] + geordnete_liste[int(entscheidungswert)]) / 2

def boxplot(daten):
    sortierte_daten = sorted(daten)
    erstes_quartil = p_quantil(sortierte_daten, 0.25)
    dieser_median = median(sortierte_daten)
    drittes_quartil = p_quantil(sortierte_daten, 0.75)
    boxhoehe = drittes_quartil - erstes_quartil
    i = 0
    ausreiszer = []
    while i < len(sortierte_daten):
        if sortierte_daten[i] > (drittes_quartil + 1.5 * boxhoehe) or sortierte_daten[i] < (erstes_quartil - 1.5 * boxhoehe):
            ausreiszer.append(sortierte_daten.pop(i))
        i += 1
    minimum = sortierte_daten[0]
    maximum = sortierte_daten[-1]
    return (erstes_quartil, dieser_median, drittes_quartil, minimum, maximum, ausreiszer)

def geometrisches_mittel(reelle_zahlen):
    """S 109"""
    summenprodukt = 1
    for zahl in reelle_zahlen:
        summenprodukt *= zahl
    return summenprodukt ** (1/len(reelle_zahlen))

def harmonisches_mittel(reelle_zahlen):
    """S 112"""
    summe = 0
    for wert in reelle_zahlen:
        summe += (1 / wert)
    return (len(reelle_zahlen) / summe)

# Kapitel 5

def spannweite(reelle_zahlen):
    """S 121"""
    return max(reelle_zahlen) - min(reelle_zahlen)

def quartilsabstand(datenreihe):
    """S 122"""
    return p_quantil(datenreihe, 0.75) - p_quantil(datenreihe, 0.25)

def durchschnittliche_mittelwertabweichung(reelle_zahlen):
    """S 124"""
    mittelwert = arithmetisches_mittel(reelle_zahlen)
    summe_der_abweichungsbetraege = 0
    for zahl in reelle_zahlen:
        summe_der_abweichungsbetraege += abs(zahl - mittelwert)
    return summe_der_abweichungsbetraege / len(reelle_zahlen)

def durchschnittliche_medianabweichung(reelle_zahlen):
    """S 124"""
    dieser_median = median(reelle_zahlen)
    summe_der_abweichungsbetraege = 0
    for zahl in reelle_zahlen:
        summe_der_abweichungsbetraege += abs(zahl - dieser_median)
    return summe_der_abweichungsbetraege / len(reelle_zahlen)

def empirische_varianz(daten):
    """
    Falls ein dict als parameter verwendet wird, geht die Funktion von einer Häufigkeitsverteilung aus. Das Format wird mit {wert:haeufigkeit} angenommen.
    """
    sum = 0
    if type(daten) == type({}):
        # S 128
        gesamtgewicht = 0
        mittel = arithmetisches_mittel(daten)
        summe_der_quadratischen_abweichung = 0
        for wert, haeufigkeit in daten.items():
            summe_der_quadratischen_abweichung += haeufigkeit * ((wert - mittel) ** 2)
            gesamtgewicht += haeufigkeit
        return summe_der_quadratischen_abweichung / (gesamtgewicht - 1)

    else:
        # S 127 Version II
        mittel = arithmetisches_mittel(daten)
        summe_der_quadratischen_abweichung = 0
        for zahl in daten:
            summe_der_quadratischen_abweichung += (zahl - mittel) ** 2
        return summe_der_quadratischen_abweichung / len(daten)

def empirische_varianz_rel_Haeufigkeit(daten):
    """
    S 128 Das Format wird mit {wert:haeufigkeit} angenommen.
    """
    sum = 0
    if type(daten) == type({}):
        # S 128
        mittel = arithmetisches_mittel(daten)
        anzahl_der_merkmale = len(daten)
        summe_der_quadratischen_abweichung = 0
        for wert, haeufigkeit in daten.items():
            summe_der_quadratischen_abweichung += haeufigkeit * ((wert - mittel) ** 2)
        return (anzahl_der_merkmale * summe_der_quadratischen_abweichung) / (anzahl_der_merkmale - 1)

def empirische_standardabweichung(varianz):
    """S 127 Version II"""
    return varianz** 0.5



