passwd = open("/etc/passwd")
lines = passwd.readlines()


shortest = "a" * 50
longest = ""

for line in lines:
    user = line.split(":")[0]

    if len(user) < len(shortest):
        shortest = user
    elif len(user) > len(longest):
        longest = user

print("The longest username is: " + longest)
print("The shortest username is: " + shortest)
