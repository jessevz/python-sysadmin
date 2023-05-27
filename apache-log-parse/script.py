#reads in apache2 log and keeps track how many bytes every client has received
import sys


def addToDict(dict, bytes, ip):
    if ip in dict:
        newBytes = bytes + dict[ip]
        dict[ip] = newBytes
    else:
        dict[ip] = bytes

def parseLine(line, dict):
    splittedLine = line.split(" ")
    recvBytes = int(splittedLine[-1])
    ip = splittedLine[0]
    addToDict(dict, recvBytes, ip)



if not len(sys.argv) > 1:
    print("Give the location of the log file as argument!")
    sys.exit(1)

try:
    logFile = open(sys.argv[1], "r")
except IOError:
    print("you have to give a valid file!")
    sys.exit(1)

dict = {}

for line in logFile:
    parseLine(line, dict)

print(dict)

    
