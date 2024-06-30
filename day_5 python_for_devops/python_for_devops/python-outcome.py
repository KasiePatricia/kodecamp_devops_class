# A module is a collection of functions to perform a task

import os

cwd = os.getcwd()

# print(cwd)

dirVariable = r"C:\Users\HP\Documents\devops\python_for_devops"

# create a directory within "python for devops"
if cwd == dirVariable:
  os.mkdir("testcode/")
else:
  os.chdir(dirVariable)