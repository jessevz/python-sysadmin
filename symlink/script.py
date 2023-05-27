import sys
import os

if len(sys.argv) < 2:
    print("Give an argument")
    sys.exit(43)

symlink = "/home/kali/python-scripting/symlink/database"

os.remove(symlink)

if sys.argv[1] == "production":
    os.symlink("/home/kali/python-scripting/symlink/production", symlink)
elif sys.argv[1] == "testing":
    os.symlink("/home/kali/python-scripting/symlink/testing", symlink)
else:
    print("Incorrect argument, specify 'production' or 'testing'")
