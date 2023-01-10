def loss_analysis(filepath, variant=True):
  """
  Executes an analysis on data from https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html
  """
  import re
  searchexpression = r'(T-\d\d)' # Search for T-xx tanks

  with open(filepath) as file:
    data = file.read()
  data = data.split('\n')

  #find vehicle category
  for line in data:
    temp = re.match(r'[A-z][ A-z]* \(', line)
    if temp != None:
      print(temp.string)
  if variant == True:
    result = []    
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<variant>' + searchexpression + r'.*)(:)', line)
      if temp != None:
        result.append(temp.groupdict())
    return result
  else:
    result = {}
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<model>' + searchexpression + r')', line)
      if temp != None:
        counter = result.get(temp.group('model'), 0)
        result[temp.group('model')] = counter + int(temp.group('number'))
    return result
