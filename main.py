import os
import subprocess
import sys
sys.dont_write_bytecode = True
import time
import requests
import colorama
from colorama import Fore, init
from pystyle import Write, Colors, Colorate

"""@a1lw and @loding_x coded this
if you're planning on skidding this code, keep this comment please and thank you mr skid man"""

init()


def banner():
    banner_text = """   
                          ███▄    █ ▓█████▄▄▄█████▓ ▄████▄  ██▀███  ▓██   ██▓
                          ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒▒██▀ ▀█ ▓██ ▒ ██▒ ▒██  ██▒
                          ▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░▒▓█    ▄▓██ ░▄█ ▒  ▒██ ██░
                          ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ ▒▓▓▄ ▄██▒██▀▀█▄    ░ ▐██▓░
                          ▒██░   ▓██░░▒████  ▒██▒ ░ ▒ ▓███▀ ░██▓ ▒██▒  ░ ██▒▓░
                          ░ ▒░   ▒ ▒ ░░ ▒░   ▒ ░░   ░ ░▒ ▒  ░ ▒▓ ░▒▓░   ██▒▒▒ 
                          ░ ░░   ░ ▒░ ░ ░      ░      ░  ▒    ░▒ ░ ▒░ ▓██ ░▒░ \n"""
    print(Colorate.Diagonal(Colors.red_to_purple, banner_text, 8))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system(f"title Netcry")
    with open("token.txt", "r") as file:
        token = file.readline().strip()
    if token == "":
        print("Empty token")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
        sys.exit(1)
    elif token == "single token here":
        print("You havent edited the file 'token.txt'.")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
        sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}
    response = requests.get("https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        data = response.json()
        user_id = data['id']
        invite_link = f"https://discord.com/api/oauth2/authorize?client_id={user_id}&permissions=8&scope=bot"
        options = f"""┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     discord.gg/9rRHUYzCHG       ┃     github.com/dropalways       ┃     github.com/dropalways       ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [1] Mass ban                   ┃  [10] . . . . . . . . . . . . . ┃  [19] . . . . . . . . . . . . . ┃
┃  [2] Mass create channels       ┃  [11] . . . . . . . . . . . . . ┃  [20] . . . . . . . . . . . . . ┃
┃  [3] Delete all channels        ┃  [12] . . . . . . . . . . . . . ┃  [21] . . . . . . . . . . . . . ┃
┃  [4] Webhook spammer            ┃  [13] . . . . . . . . . . . . . ┃  [22] . . . . . . . . . . . . . ┃
┃  [5] Webhook deleter            ┃  [14] . . . . . . . . . . . . . ┃  [23] . . . . . . . . . . . . . ┃
┃  [6] Nuker bot                  ┃  [15] . . . . . . . . . . . . . ┃  [24] . . . . . . . . . . . . . ┃
┃  [7] Channel spammer            ┃  [16] . . . . . . . . . . . . . ┃  [25] . . . . . . . . . . . . . ┃
┃  [8] Give admin to a user       ┃  [17] . . . . . . . . . . . . . ┃  [26] . . . . . . . . . . . . . ┃
┃  [9] Mass create roles          ┃  [18] . . . . . . . . . . . . . ┃  [27] . . . . . . . . . . . . . ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃    {invite_link}   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
        banner()
        print(Colorate.Vertical(Colors.purple_to_red, options, 1))
    else:
        optionsi = """┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃     discord.gg/9rRHUYzCHG       ┃     github.com/dropalways       ┃     github.com/dropalways       ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [1] Mass ban                   ┃  [10] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [2] Mass create channels       ┃  [11] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [3] Delete all channels        ┃  [12] . . . . . . . . . . . . . ┃   [10] . . . . . . . . . . . . .┃
┃  [4] Webhook spammer            ┃  [13] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [5] Webhook deleter            ┃  [14] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [6] Nuker bot                  ┃  [15] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [7] Channel spammer            ┃  [16] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [8] Give admin to a user       ┃  [17] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┃  [9] Mass create roles          ┃  [18] . . . . . . . . . . . . . ┃  [10] . . . . . . . . . . . . . ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
        banner()
        print(Colorate.Vertical(Colors.purple_to_red, optionsi, 1))

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
        elif user_input == "9":
            subprocess.run(["python", "commands/massrole.py"])
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