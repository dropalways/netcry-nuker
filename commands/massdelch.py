import aiohttp
import asyncio
import json

async def delete_channel(session, channel_id, headers):
    url = f'https://discord.com/api/v9/channels/{channel_id}'
    async with session.delete(url, headers=headers) as response:
        if response.status == 200:
            print(f"Channel '{channel_id}' deleted successfully.")
        elif response.status == 429:
            print("Rate limited waiting 0.7 seconds...")
            await asyncio.sleep(0.7)
        else:
            print(f"Failed to delete channel '{channel_id}'. Status code: {response.status}")

async def delete_category(session, category_id, headers):
    url = f'https://discord.com/api/v9/channels/{category_id}'
    async with session.delete(url, headers=headers) as response:
        if response.status == 200:
            print(f"Category '{category_id}' deleted successfully.")
        elif response.status == 429:
            print("Rate limited waiting 0.7 seconds...")
            await asyncio.sleep(0.7)
        else:
            print(f"Failed to delete category '{category_id}'. Status code: {response.status}")

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

    async with aiohttp.ClientSession() as session:
        channels_url = f'https://discord.com/api/v9/guilds/{target_id}/channels'
        async with session.get(channels_url, headers=headers) as response:
            if response.status == 200:
                channels_data = await response.json()

                tasks = []
                for channel in channels_data:
                    channel_id = channel['id']
                    channel_type = channel['type']

                    if channel_type == 4:  # Category
                        tasks.append(delete_category(session, channel_id, headers))
                    else:  # Text or Voice Channel
                        tasks.append(delete_channel(session, channel_id, headers))

                await asyncio.gather(*tasks)

            elif response.status == 429:
                print("Rate limited, waiting 0.7 seconds...")
                await asyncio.sleep(0.7)
            else:
                print(f"Failed to fetch channels. Status code: {response.status}")

asyncio.run(main())
