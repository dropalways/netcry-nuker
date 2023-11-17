import aiohttp
import asyncio
import os
import sys


async def main():
    with open("token.txt", "r") as file:
        token = file.readline().strip()
        if token == "":
            print("Empty token")
            sys.exit(1)
        elif token == "single token here":
            print("You haven't edited the file 'token.txt'.")
            sys.exit(1)

    question = input("Are you using a selfbot? (y/n) ")
    if question == "y":
        headers = {"Authorization": token}
        await massleave(headers)
    elif question == "n":
        headers = {"Authorization": f"Bot {token}"}
        await massleave(headers)
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("That's not a valid choice")
        await main()


async def massleave(headers):
    whitelist = input("Do you want to whitelist any servers to not leave? (y/n): ")
    whitelistids = []
    if whitelist.lower() == "y":
        while True:
            guild_id = input("Enter a guild id you want to whitelist (or enter nothing to stop): ")
            if not guild_id:
                break
            whitelistids.append(guild_id)
    elif whitelist.lower() == "n":
        pass
    else:
        print("That's not a valid choice.")
        await massleave(headers)

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get("https://discord.com/api/v9/users/@me/guilds") as response:
            if response.status == 200:
                data = await response.json()

                guild_ids = [guild['id'] for guild in data]

                non_whitelisted_ids = [guild_id for guild_id in guild_ids if guild_id not in whitelistids]

                for non_whitelisted_id in non_whitelisted_ids:
                    async with session.delete(
                            f"https://discord.com/api/v9/users/@me/guilds/{non_whitelisted_id}") as leave_response:
                        print(f"Left {non_whitelisted_id}")
            else:
                print("Failed to retrieve guilds. Status code:", response.status)


if __name__ == "__main__":
    asyncio.run(main())
