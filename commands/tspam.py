import requests
import time
import sys

def spam():
    global successful

    while successful < num:
        response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json)
        if response.status_code == 200:
            successful += 1
            print(f"Message sent! ({successful}/{num})")
            time.sleep(0.2)
        elif response.status_code == 429:
            print("Ratelimited, waiting 3 seconds...")
            time.sleep(3)
        else:
            print(f"Error occurred {response.status_code}")

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

stoken = input("Is this a user token? [y/n] ")
if stoken == "y":
    headers = {'Authorization': f'{token}'}
elif stoken == "n":
    headers = {'Authorization': f'Bot {token}'}
else:
    print("Incorrect answer")
    sys.exit(1)

message = input("Message? ")
num = int(input("How many messages? "))
channel_id = input("Channel id? ")
json = {"content": f'{message}'}
successful = 0
spam()
