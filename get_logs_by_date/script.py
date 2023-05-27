import sys

if len(sys.argv) < 2:
    print("Give the date of the log files you want to see in format Month-Day!")
    sys.exit(3)

userInput = sys.argv[1].split("-")

if len(userInput) != 2:
    print("Invallid input. Give in format Month-Day!")
    sys.exit(4)

try:
    month = userInput[0]
    day = userInput[1]
    int(month)
    int(day)

except ValueError:
    print("Invallid input! Give month and day in number value!")
    sys.exit(5)


date = f"2023-{month}-{day}"
print(date)

with open("/var/log/syslog") as file:
    for line in file:
        if line.split("T")[0] == date:
            print(line)