from pystyle import Write, Colors
from colorama import Fore, init
import requests
import time
import os
import subprocess
import sys

sys.dont_write_bytecode = True

init()

commands = {
    "1": "massban",
    "2": "masschannel",
    "3": "massdelch",
    "4": "webhook",
    "5": "dwebhook",
    "6": "nuker",
    "7": "tspam",
    "8": "givadmin",
    "9": "massrole",
    "10": "dallmessage",
    "11": "massleave",
    #   "exit": sys.exit,
    "mass ban": "massban",
    #   "reload": "reload",
}


def banner():
    banner_text = """
                                                   __                 
                                       ____  ___  / /_____________  __
                                      / __ \/ _ \/ __/ ___/ ___/ / / /
                                     / / / /  __/ /_/ /__/ /  / /_/ / 
                                    /_/ /_/\___/\__/\___/_/   \__, /
                                                             /____/
"""
    print(Fore.MAGENTA + banner_text)


def main():
    os.system('clear' if os.name != 'nt' else 'cls')
    os.system(f"title Netcry")
    with open("token.txt", "r") as file:
        token = file.readline().strip()
    if token == "":
        print("Empty token")
        sys.exit(1)
    elif token == "single token here":
        print("You havent edited the file 'token.txt'.")
        sys.exit(1)

    headers = {'Authorization': f'Bot {token}'}
    response = requests.get(
        "https://discord.com/api/v9/users/@me", headers=headers)

    if response.status_code == 200:
        data = response.json()
        user_id = data['id']
        invite_link = f"https://discord.com/api/oauth2/authorize?client_id={user_id}&permissions=8&scope=bot"
        options = f"""{Fore.LIGHTMAGENTA_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {Colors.gray}https://discord.gg/9rRHUYzCHG{Fore.LIGHTMAGENTA_EX}  ┃       {Colors.gray}https://e-z.bio/az{Fore.LIGHTMAGENTA_EX}        ┃  {Colors.gray}https://github.com/dropalways{Fore.LIGHTMAGENTA_EX}  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [{Colors.gray}1{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass ban{Fore.LIGHTMAGENTA_EX}                   ┃  [{Colors.gray}10{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass purge messages{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}19{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}2{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create channels{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}11{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass leave servers{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}20{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}3{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Delete all channels{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}12{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}21{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}4{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}13{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}22{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}5{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook deleter{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}14{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}23{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}6{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Nuker bot{Fore.LIGHTMAGENTA_EX}                  ┃  [{Colors.gray}15{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}24{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}7{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Channel spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}16{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}25{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}8{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Give admin to a user{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}17{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}26{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}9{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create roles{Fore.LIGHTMAGENTA_EX}          ┃  [{Colors.gray}18{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}27{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃    {Colors.gray}{invite_link}{Fore.LIGHTMAGENTA_EX}   ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
        banner()
        print(Fore.LIGHTMAGENTA_EX + options)
    else:
        options2 = f"""{Fore.LIGHTMAGENTA_EX}┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  {Colors.gray}https://discord.gg/9rRHUYzCHG{Fore.LIGHTMAGENTA_EX}  ┃       {Colors.gray}https://e-z.bio/az{Fore.LIGHTMAGENTA_EX}        ┃  {Colors.gray}https://github.com/dropalways{Fore.LIGHTMAGENTA_EX}  ┃
┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
┃  [{Colors.gray}1{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass ban{Fore.LIGHTMAGENTA_EX}                   ┃  [{Colors.gray}10{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass purge messages{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}19{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}2{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create channels{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}11{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass leave servers{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}20{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}3{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Delete all channels{Fore.LIGHTMAGENTA_EX}        ┃  [{Colors.gray}12{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}21{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}4{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}13{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}22{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}5{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Webhook deleter{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}14{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}23{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}6{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Nuker bot{Fore.LIGHTMAGENTA_EX}                  ┃  [{Colors.gray}15{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}24{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}7{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Channel spammer{Fore.LIGHTMAGENTA_EX}            ┃  [{Colors.gray}16{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}25{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}8{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Give admin to a user{Fore.LIGHTMAGENTA_EX}       ┃  [{Colors.gray}17{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}26{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┃  [{Colors.gray}9{Fore.LIGHTMAGENTA_EX}] {Colors.gray}Mass create roles{Fore.LIGHTMAGENTA_EX}          ┃  [{Colors.gray}18{Fore.LIGHTMAGENTA_EX}] {Colors.gray}. . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃  [{Colors.gray}27{Fore.LIGHTMAGENTA_EX}] . . . . . . . . . . . . .{Fore.LIGHTMAGENTA_EX} ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛"""
        banner()
        print(options2)

    while True:
        try:
            user_input = Write.Input(f"\n\ntrollinc""@netcry━>>> ", Colors.gray, interval=0.03)

        except KeyboardInterrupt:
            sys.exit()

        user_input = user_input.lower()

        if user_input in commands:
            if user_input == "exit":
                commands[user_input]()
            else:
                try:
                    subprocess.run(["python", str(f"commands/{commands.get(user_input)}.py")])
                except KeyboardInterrupt:
                    sys.exit()
        elif user_input == "":
            print("Error: Enter something")
            time.sleep(0.7)
            main()
        elif user_input == "reload":
            main()
        else:
            print(Fore.RED + "Error 404: Command not found")
            time.sleep(0.7)
            main()


if __name__ == "__main__":
    main()
