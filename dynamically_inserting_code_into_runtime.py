# wrapper to execute dynamic code
# the "external" code is executed in the main frame (__name__ == '__main__' evaluates to True and variables are changed).
# this wrapper only works for "external" code that completes in relativly short time - otherwise the whole thing is pointless.
#ADD check code for updates every day at around 0300L
#ENHANCE include an option to manually trigger an update_check
#ENHANCE avoid reading and processing large files by checking a version number and skipping if up-to-date (checksum? versionnumber in seperate file?)
#OPTIONAL enable on-the-fly wrapper paramter changes (eg time of regular update check)

import time

update_done = False

while True:
  try:
    with open("/content/drive/MyDrive/Colab Notebooks/dynamic_code_test/test.py") as code:
      code = code.read()
    exec(code)
  except:
    print("Could not open file.")
  del code

  if not update_done and time_for_update():
    try:
      with open("/content/drive/MyDrive/Colab Notebooks/dynamic_code_test/function.py") as code:
        code = code.read()
      exec(code)
      update_done = True
    except:
      print("Could not open file. Will try again in next cycle.")
  # countdown to avoid conflicting file access
  for i in range(9, 0, -1):
    print(i)
    time.sleep(1)
    print("\b\b", end="")
