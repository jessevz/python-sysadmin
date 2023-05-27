from subprocess import run
import sys

if len(sys.argv) < 2:
    print("Give user")
    sys.exit(43)

username = sys.argv[1]

output = run(["ps", "-aux"], capture_output=True, text=True)#.stdout.strip("\n")

# print(output)

for line in output.stdout.split("\n"): 
    if not line:
        break
    split = line.split()
    usr = split[0]
    uid = split[1]

    if usr == username:
        print(uid)
