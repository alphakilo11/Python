def loss_analysis(filepath, variant=True):
  """
  Executes an analysis of data from 
  """
  import re
  searchexpression = r'T-\d\d'
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