import os, sys
import os.path

def loop_through_files(rootdir, inode):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if os.stat(os.path.join(subdir,file)).st_ino == inode:
                print(os.path.join(subdir,file))
                sys.exit(0)
        for dir in dirs:
            loop_through_files(dir, inode)


if len(sys.argv) < 3:
    print("Give the innode and directory")
    sys.exit(2)

rootdir = sys.argv[1]

if not sys.argv[2].isnumeric():
    print("Invallid")
    sys.exit(3) 

inode = int(sys.argv[2])


loop_through_files(rootdir, inode)

print("No file found with that inode!")
sys.exit(1)
