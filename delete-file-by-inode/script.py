import os
import sys
#removes file by inode in current dir

if len(sys.argv) < 2:
    print("Give inode of the file that has to be removed!")
    sys.exit(3)


inode = int(sys.argv[1])
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    if inode == os.stat(f).st_ino:
        os.remove(f)
        print(f"removed: {f}")
        sys.exit(0)

print("Inode not found in current working directory!")
sys.exit(2)