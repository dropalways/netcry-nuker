import aiohttp
import asyncio
import json

async def create_channel(session, target_id, channel_name, channel_type, headers):
    data = {'name': channel_name, 'type': channel_type}
    url = f'https://discord.com/api/v9/guilds/{target_id}/channels'
    async with session.post(url, json=data, headers=headers) as response:
        if response.status == 201:
            print(f"Channel '{channel_name}' created successfully.")
        elif response.status == 429:
            print("Rate limited, waiting 0.7 seconds...")
            await asyncio.sleep(0.7)
        else:
            print(f"Failed to create channel '{channel_name}'. Status code: {response.status}")

async def main():
    with open("token.txt", "r") as file:
        token = file.readline().strip()

    if token == "":
        print("Empty token in token.txt")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
        return

    selfbot = input("Selfbot? [y|n] ")
    if selfbot == "y":
        bottoken = True
    elif selfbot == "n":
        bottoken = False
    else:
        print("Invalid answer")
        return

    if not bottoken:
        headers = {'Authorization': f'Bot {token}', 'Content-Type': 'application/json'}
    else:
        headers = {'Authorization': f'{token}', 'Content-Type': 'application/json'}

    target_id = input("Target guild ID: ")
    channel_name = input("Channel name: ")
    how_many = input("Number of channels to create: ")
    vc_or_text = input("Text channel or voice channel? [t|vc] ")
    if vc_or_text == "t":
        channel_type = 0
    elif vc_or_text == "vc":
        channel_type = 2
    else:
        print("Invalid option...")
        return

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(int(how_many)):
            tasks.append(create_channel(session, target_id, channel_name, channel_type, headers))

        await asyncio.gather(*tasks)

asyncio.run(main())
