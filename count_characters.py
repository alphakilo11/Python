# this is also very handy to check for Umlauts

text = '# Berechnung bedrohter Flaeche \
# TODO find a way to include sliders\
# import ipywidgets as widgets \
# slider = widgets.IntSlider(value=5, max=10)\
# display(slider)\
\
def time_on_target(a, b, speed):\
  """returns the time in seconds it takes an object moving at speed to travel the geodesic distance from point a to point b\
  Parameters: a, b  LATLONG coordinates\
              speed: m/s\
  """\
  from geopy.distance import geodesic\
  return geodesic(a, b).m / speed\
\
def create_grid(loc, long, lat, deep, resolution):\
  """\
  TODO change depth to altitude(feet)\
  returns a list of coordinates creating a grid with given latitude (grade), longitude (grade), depth(nm) and resolution (grade) at given location (coordinate)\
  depth 0 returns an empty list\
  """\
  from geopy.distance import geodesic\
  coordinates = []\
  len_increment = round(long / resolution)\
  wid_increment = round(lat / resolution)\
  dep_increment = 1 # dummy \
  for i in range(len_increment):\
    for j in range(wid_increment):\
      for k in range(dep_increment):\
        coordinates.append([loc[0] + resolution * i, loc[1] + resolution * j, k])\
  return coordinates\
#--------------------------------------\
ftr_speed = mach(-0.95, conv_ft_m(13000))\
ftr_bvz = 11 * 60\
ftr_base = [47.203889, 14.747778]\
\
tgt_speed = conv_kt_ms(514)\
tgt_base = [48.51911, 20.17096] \
\
\
#draw Map\
m = folium.Map(location=tgt_destination, width="100%", height="100%", zoom_start=8, tiles="OpenStreetMap")\
\
coordinates = create_grid([46, 13], 3, 4, 1, 0.1)\
for i in coordinates:\
  if (time_on_target(ftr_base, i, ftr_speed) + ftr_bvz) <= time_on_target(tgt_base, i, tgt_speed):\
    farbe = "blue"\
  else:\
    farbe = "red"\
  folium.vector_layers.Circle(location=i, radius=1, color=farbe).add_to(m)\
\
m'
count = {}
for i in text:
  count.setdefault(i, 0)
  count[i] = count[i] + 1
count
