from colorama import Fore, Back, Style
import time

for i in range(20):
    for j in range(166):
        if i <= 9:
            print(Fore.RED+"*",end="")
        elif i <= 20:
            print(Fore.WHITE + "*", end="")

    time.sleep(0.5)
    print()