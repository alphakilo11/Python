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

