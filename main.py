import os
import subprocess
import sys
sys.dont_write_bytecode = True
import time

import colorama
from colorama import Fore, init
from pystyle import Center, Write, Colors, Colorate

"""@a1lw and @loding_x coded this
if you're planning on skidding this code, keep this comment please and thank you mr skid man"""

init()

options = """
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     discord.gg/9rRHUYzCHG       ┃     github.com/dropalways/      ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [1] Mass ban                   ┃  [10]                           ┃
┃  [2] Mass create channels       ┃  [11]                           ┃
┃  [3] Delete all channels        ┃  [12]                           ┃
┃  [4] Webhook spammer            ┃  [13]                           ┃
┃  [5] Webhook delete             ┃  [14]                           ┃
┃  [6] Nuker bot                  ┃  [15]                           ┃
┃  [7] Channel spammer            ┃  [16]                           ┃
┃  [8] Give admin to a user       ┃  [17]                           ┃
┃  [9]                            ┃  [18]                           ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
"""

def banner():
    banner_text = """ ███▄    █ ▓█████▄▄▄█████▓ ▄████▄  ██▀███  ▓██   ██▓
 ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▒██▀ ▀█ ▓██ ▒ ██▒ ▒██  ██▒
▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒▓█    ▄▓██ ░▄█ ▒  ▒██ ██░
▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒▓▓▄ ▄██▒██▀▀█▄    ░ ▐██▓░
▒██░   ▓██░░▒████  ▒██▒ ░ ▒ ▓███▀ ░██▓ ▒██▒  ░ ██▒▓░
░ ▒░   ▒ ▒ ░░ ▒░   ▒ ░░   ░ ░▒ ▒  ░ ▒▓ ░▒▓░   ██▒▒▒ 
░ ░░   ░ ▒░ ░ ░      ░      ░  ▒    ░▒ ░ ▒░ ▓██ ░▒░ 
   ░   ░ ░    ░    ░ ░    ░          ░   ░  ▒ ▒ ░░  
         ░    ░           ░ ░        ░      ░ ░     """
    print(Colorate.Diagonal(Colors.red_to_purple, banner_text, 8))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Netcry")
    banner()
    print(Colorate.Vertical(Colors.purple_to_red, options, 1))
    while True:
        user_input = Write.Input(f"\n\ntrollinc""@netcry━>>> ", Colors.blue_to_red, interval=0.03)
        user_input = user_input.lower()
    
        if user_input == "1":
            subprocess.run(["python", "commands/massban.py"])
            time.sleep(1.9)
            main()
        elif user_input == "":
            print("Error enter something")
            time.sleep(0.7)
            main()
        elif user_input == "2":
            subprocess.run(["python", "commands/masschannel.py"])
            time.sleep(1.9)
            main()
        elif user_input == "3":
            subprocess.run(["python", "commands/massdelch.py"])
            time.sleep(1.9)
            main()
        elif user_input == "4":
            subprocess.run(["python", "commands/webhook.py"])
            time.sleep(1.9)
            main()
        elif user_input == "5":
            subprocess.run(["python", "commands/dwebhook.py"])
            time.sleep(1.9)
            main()        
        elif user_input == "6":
            subprocess.run(["python", "commands/nuker.py"])
            time.sleep(1.9)
            main()
        elif user_input == "7":
            subprocess.run(["python", "commands/tspam.py"])
            time.sleep(1.9)
            main()
        elif user_input == "8":
            subprocess.run(["python", "commands/givadmin.py"])
            time.sleep(1.9)
            main()
        elif user_input == "exit":
            sys.exit()
        else:
            print(Fore.RED +"Error 404: Command not found")
            time.sleep(0.7)
            main()

if __name__ == "__main__":
    main()