# (create and) write to file
with open("foo.txt", "w") as bar:
  bar.write(str(spam))

# read from file  
with open("foo.txt") as spam:
  foo = spam.read()
