import sys
sys.dont_write_bytecode = True
import colorama
from colorama import Fore, init
from pystyle import Center
import os
import time

init()

def banner():
    banner_text = (Fore.RED + """ ███▄    █ ▓█████▄▄▄█████▓ ▄████▄  ██▀███  ▓██   ██▓
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▒██▀ ▀█ ▓██ ▒ ██▒ ▒██  ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒▓█    ▄▓██ ░▄█ ▒  ▒██ ██░
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒▓▓▄ ▄██▒██▀▀█▄    ░ ▐██▓░
▒██░   ▓██░░▒████  ▒██▒ ░ ▒ ▓███▀ ░██▓ ▒██▒  ░ ██▒▓░
░ ▒░   ▒ ▒ ░░ ▒░   ▒ ░░   ░ ░▒ ▒  ░ ▒▓ ░▒▓░   ██▒▒▒ 
░ ░░   ░ ▒░ ░ ░      ░      ░  ▒    ░▒ ░ ▒░ ▓██ ░▒░ 
   ░   ░ ░    ░    ░ ░    ░          ░   ░  ▒ ▒ ░░  
         ░    ░           ░ ░        ░      ░ ░     """)
    print(banner_text)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system("title ball")
    banner()
    while True:
        user_input = input(Fore.CYAN +"\n\n--trollinc"+ Fore.RED +"@netcry->>> ")
        user_input = user_input.lower()
    
        if user_input == "1":
            subprocess.run(["python", "commands/"])
            
        else:
            print("Error 404 command not found")
            time.sleep(0.7)
            main()

if __name__ == "__main__":
    main()
