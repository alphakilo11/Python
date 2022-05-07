test = open(r'/content/sample_data/README.md').read() # this file is available in Google Colaboratory
filelist = test.split("\n")
for i in range(len(filelist)):
  filelist[i] = "* " + filelist[i]
filelist = "\n".join(filelist)
print(filelist)