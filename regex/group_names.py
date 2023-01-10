def loss_analysis(filepath, variant=True):
  """
  Executes an analysis on data from https://www.oryxspioenkop.com/2022/02/attack-on-europe-documenting-equipment.html
  """
  import re
  searchexpression = r'T-\d\d' # Search for T-xx tanks
  with open(filepath) as file:
    data = file.read()
  data = data.split('\n')
  result = []
  if variant == True:
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<variant>' + searchexpression + r'.*)(:)', line)
      if temp != None:
        result.append(temp.groupdict())
    return result
  else:
    for line in data:
      temp = re.search(r'(?P<number>\d+)(\s|\sUnknown\s)(?P<model>' + searchexpression + r')', line)
      if temp != None:
        result.append(temp.groupdict())
    return result    