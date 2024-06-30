import os
import sys
import subprocess

command = ["vagrant", "init", "ubuntu/focal64"]
command2 = ["vagrant", "up"]

dirPath = r"C:\Users\HP\Documents\devops\python_for_devops"

sp = subprocess.Popen(command,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
sp2 = subprocess.Popen(command2,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

# function definition
def get_version():
  version = sys.version

  versionID = version[0:6]
  return versionID


def create_folder():
  print("\nCreating folder")

  vid = get_version()

  if "3" in vid:
    os.mkdir("kc4_osfolder-%s" % vid)


def chDir():
  os.chdir("resources")

def resource():
  dir = os.getcwd()

  if dir == dirPath:
    os.mkdir("resources")
    chDir()
  else:
    os.chdir(dirPath)
    os.mkdir("resources")
    chDir()

def create_resources():
  resource()
  sp
  sp2


def main():
  print("Executing main function...")

  print( get_version())

  create_folder()

  create_resources()
  

main()