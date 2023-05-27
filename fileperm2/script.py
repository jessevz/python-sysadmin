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
import sys

def create_file(file, directory, permission, user, group):
    file_path = os.path.join(directory, file)
    f = open(file_path, "x")
    try:
        os.chmod(file_path, permission)
        uid = pwd.getpwnam(user).pw_uid
        guid = grp.getgrnam(group).gr_gid
        os.chown(file_path, uid, guid)
    except PermissionError:
        print(f"Incorrect permissions to change owner/group of file {file_path}!")
        os.remove(file_path)
        sys.exit(2)


directory = "backup"
parent_dir = "/home/kali/python-scripting/fileperm2"

path = os.path.join(parent_dir, directory)

if not os.path.exists(path):
    os.mkdir(path)

create_file("secret.txt", path, 0o600, "root", "root")
create_file("wheelonly.txt", path, 0o060, "root", "wheel")
create_file("test.txt", path, 0o777, "kali", "kali")
create_file("script.sh", path, 0o474, "kali", "docker")
create_file("useronly.txt", path, 0o644, "kali", "kali")


