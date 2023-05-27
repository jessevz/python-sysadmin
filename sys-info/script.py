import subprocess
import sys

info = """
Sys info menu:
1.  Currently logged in users
2.  your shell directory
3.  Home directory
4.  Os name & version
5.  Current working directory
6.  number of users logged in
7.  Show all available shellsin your system
8.  Hard disk information
9.  CPU information
10.  Memory information
11.  File system information
12.  Currently running processes
13.  Currently logged in users
"""

print(info)

userInput = int(input().strip())

if userInput == 1:
    subprocess.run(["whoami"])
elif userInput == 2:
    subprocess.run(["pwd"])
elif userInput == 3:
    subprocess.run(["sh", "-c", "echo", "$HOME"])
elif userInput == 4:
    subprocess.run(["uname", "-r"])
elif userInput == 5:
    subprocess.run(["pwd"])
elif userInput == 6:
    
else:
    print("invallid input!")
    sys.exit(23)
