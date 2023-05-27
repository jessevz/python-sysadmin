from datetime import datetime
import sys, os

directory = "backups"
cwd = os.getcwd()
path = os.path.getmtime

for file in os.listdir(directory):
    print(os.path.getmtime(cwd + "/" + directory + "/" + file))
    print(datetime.fromtimestamp(os.path.getmtime(cwd + "/" + directory + "/" + file)).year)
    