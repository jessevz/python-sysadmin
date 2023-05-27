passwd = open("/etc/passwd")
lines = passwd.readlines()


for line in lines:
    uid = int(line.split(":")[2])
    usr = line.split(":")[0]
    if uid > 1000:
        print(usr)
