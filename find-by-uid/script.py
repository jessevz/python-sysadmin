from pwd import getpwnam  
from subprocess import Popen, PIPE
import os
import sys

if len(sys.argv) < 3:
    print("Give path and username")
    sys.exit(43)

username = sys.argv[1]

try:
    uid = getpwnam(username)[2]
except KeyError:
    print("User doesnt exists!")
    sys.exit(43)

directory = sys.argv[2]

if (not os.path.exists(directory)):
    print("invallid directory!")
    sys.exit(43)

for root,d_names,f_names in os.walk(directory):
	# print (root, d_names, f_names)
    for file in f_names:
        filePath = root + "/" + file
        if (os.path.isfile(filePath) and os.stat(filePath).st_uid == uid):
            # print(os.stat(filePath))
            print(filePath)
