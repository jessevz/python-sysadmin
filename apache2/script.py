import os  # I think it's better to use subprocess for this. but quick code for example
import time
# status = os.system('systemctl is-active --quiet apache2')


while True:
    status = os.system('systemctl is-active --quiet apache2')
    if status == 0:
        print(".", end="", flush=True)
    else:
        print()
        os.system("service apache2 status")
        break
    time.sleep(1)


