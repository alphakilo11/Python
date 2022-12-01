
#!pip install great-circle-calculator
import folium
ankerpunkt = (47.5, 16)

def reverse_elements(coordinate):
  """switches first and second element"""
  return [coordinate[1], coordinate[0]]

def rectangle_coordinates(ursprung, latitude, longitude):
  """
  BUG longitude is way too short (latitude is fine)
  SOLUTION https://geopy.readthedocs.io/en/stable/#module-geopy.distance
  ursprung = südwestecke
  length = nord-süd Ausdehnung
  with = ost-west Ausdehnung
  """
  import great_circle_calculator.great_circle_calculator as gcc
  return gcc.point_given_start_and_bearing(gcc.point_given_start_and_bearing(ursprung, 90, latitude, unit='meters'), 0, longitude, unit='meters') # course=0 bedeutet Richtung 90°, course=90 bedeutet Richtung 360°

m = folium.Map(location=ankerpunkt, zoom_start=9)

folium.vector_layers.Rectangle(
    bounds=[ankerpunkt, rectangle_coordinates(ankerpunkt, 144e3, 72e3)]
).add_to(m)

m

from geopy.distance import geodesic
coordinate1 = (48.856613, 2.352222)
coordinate2 = (55.755833, 37.617222)
distance_in_miles = geodesic(coordinate1, coordinate2).miles
distannce_in_km = geodesic(coordinate1, coordinate2).km
print(distannce_in_km)
