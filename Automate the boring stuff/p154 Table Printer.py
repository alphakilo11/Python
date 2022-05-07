def findmax(list_of_strings):
  max = 0
  for i in list_of_strings:
    if len(i) > max:
      max = len(i)
  return max

tableData = [
             ["dice", "apples", "bananas", "hotdogs", "wheat"],
             ["Carol", "Bob", "Richard", "Carl", "Uriel Septim"],
             ["Suchoi", "MiG", "McDonell", "Martin", "EADS"]
]

# determine longest string in each column and safe to a list
while True:
  abort = 0
  maxima = []
  for i in tableData:
    maxima.append(findmax(i))

  rows = findmax(tableData)
  for list in tableData:
    if len(list) < rows:
      print("Error: all lists have to have the same number of entries")
      abort = 1
      break
  if abort == 1:
    break


  for i in range(rows):
    for j in range(len(maxima)):
      print(tableData[j][i].rjust(maxima[j]), end=" ")
    print()
  break