import subprocess
import sys

if len(sys.argv) < 2:
    print("Give atleast 1 file to backup")
    sys.exit(3)

command = ["tar", "-czvf", "backup.tar.gz"] + sys.argv[1:]


try:
    subprocess.check_output(command, stderr=subprocess.DEVNULL)
except:
    print("invallid file(s)!")
    sys.exit(4)
