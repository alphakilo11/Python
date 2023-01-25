def loss_analysis(filepath, variant=True):
  """
  Executes an analysis on data from https://www.oryxspioenkop.com
  Russian losses: https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html
  Ukrainian losses: https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-ukrainian.html
  """
  import re
  searchexpression = r'(T-\d\d)' # Search for T-xx tanks

  with open(filepath) as file:
    data = file.read()

  #find vehicle category
  categories = []
  temp = re.findall(r'([A-z][ A-z]*)( \()', data)
  if temp != None:
    print(len(temp))
    #for i in range(1, len(temp), 2):
    #  print(temp[i])
    #categories.append(temp.group('category'))
  #print(categories)

  data = data.split('\n')
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