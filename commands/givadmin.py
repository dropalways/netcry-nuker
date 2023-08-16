import requests
import json

def ball():
    with open("token.txt", "r") as file:
        token = file.readline().strip()

    if token == "":
        print("Empty token")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
    elif token == "single token here":
        print("You havent edited the file 'token.txt'.")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
    else:
        print("This will only work with bot tokens")
        main(token)


def create_role(token, guild_id, user_id, rname):
    create_role_url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    
    headers = {
        "Authorization": f"Bot {token}",
        "Content-Type": "application/json"
    }

    data = {
        "name": f"{rname}",
        "permissions": "8",
        "color": 0,
        "hoist": False,
        "mentionable": False
    }

    response = requests.post(create_role_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        role_data = response.json()
        role_id = role_data['id']
        return role_id
    else:
        print(f"Failed to create role. Status Code: {response.status_code}")
        return None


def assign_role(token, role_id, guild_id, user_id):
    modify_member_role_url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}/roles/{role_id}"
    
    headers = {
        "Authorization": f"Bot {token}"
    }
    response = requests.put(modify_member_role_url, headers=headers)

    if response.status_code == 204:
        print("Role assigned successfully!")
    else:
        print(f"Failed to assign role to the user. Status Code: {response.status_code}")


def main(token):
    guild_id = input("Enter the target guild id: ")
    user_id = input("Enter the target user id to get admin: ")
    rname = input("Enter the role name: ")
    role_id = create_role(token, guild_id, user_id, rname)
    print(f"Created role {role_id}")
    if role_id:
        assign_role(token, role_id, guild_id, user_id)


ball()
