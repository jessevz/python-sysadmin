import os
from time import sleep
while True:
    status = os.system("systemctl is-active --quiet apache2")
    if status > 0:
        os.system("service apache2 status")
        break
    print(".", end="", flush=True)
    sleep(1)
