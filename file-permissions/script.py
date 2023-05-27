"""
-rw------- root root secret.txt
----rw---- root wheel wheelonly.txt
-rwxrwxrwx kali kali test.txt
-r--rwxr--  1 kali docker  script.sh
-rw-r--r--  1 kali kali useronly.txt
"""
import os
import pwd
import grp

directory = "backup"
parent_dir = "/home/kali/python-scripting/file-permissions"
path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
    os.mkdir(path)

class File:
    def __init__(self, fileName, group, user, permissions):
        self.fileName = fileName
        self.group = group
        self.user = user
        self.permissions = permissions


files = []
files.append(File("secret.txt", "root", "root", 0o600))
files.append(File("wheelonly.txt", "wheel", "root", 0o060))
files.append(File("test.txt", "kali", "kali", 0o777))
files.append(File("script.sh", "docker", "kali", 0o464))
files.append(File("useronly.txt", "root", "root", 0o600))

for file in files:
    filePath = os.path.join(path, file.fileName)
    f = open(filePath, "w+")
    os.chmod(filePath, file.permissions)

    uid = pwd.getpwnam(file.user).pw_uid
    gid = grp.getgrnam(file.group).gr_gid
    os.chown(filePath, uid, gid)


