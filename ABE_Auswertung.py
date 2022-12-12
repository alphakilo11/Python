def ABE_auswertung(folderpath):
  """
  extracts Automated Battle Engine results from Arma 3 rpt files
  Example:
    print(ABE_auswertung("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1"))
  ENHANCE use regex
  ENHANCE include datetime (filename + timestamp) - but what's the benefit?
  ENHANCE ignore other files
  """
  from os import listdir
  from os.path import isfile, join
  file_list = [f for f in listdir(folderpath) if isfile(join(folderpath, f))]
  step1 = ''
  for file in file_list:
    with open((folderpath + '/' + file), 'r') as datei:
      step1 += datei.read()
  step1 = step1.split('\n')
  # get Result Lines
  step2 = []
  for line in step1:
    if 'AKBL Result: Survivors:' in line:
      step2.append(line)
  del step1
  # break apart Result Lines
  step3 = []
  for line in step2:
    step3.append(line.split('Survivors: ')[1])
  del step2
  # break apart further
  step4 = []
  for line in step3:
    step4.append((line.split('.')[0].split(';')))
  del step3

  return step4

def ABE_aufbereitung(daten):
  """
  Soll die Daten übersichticher darstellen.
  """
  output = []
  for line in daten:
    daheim = int(line[1])
    auswaerts = int(line[3])
    if daheim > auswaerts:
      result = 'WON'
    elif daheim < auswaerts:
      result = 'LOST'
    else:
      result = 'DRAW'
    output.append((line[0],result, line[2], line[1] , line[3]))
  return output

def create_matrix(data):
  """
  Create a matrix
  Example:
    print(create_matrix(ABE_auswertung("/content/drive/MyDrive/ArmA 3/Homebrew/Automated Battle Engine/Results_1")))
  """
  entries = []
  for line in data:
    entries.append(line[0])
    entries.append(line[2])
  return sorted(set(entries)) # collect all
