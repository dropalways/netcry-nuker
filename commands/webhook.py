import asyncio
import aiohttp

async def send_message(session, webhook_url, message_content, username, successful_messages, num_messages):
    payload = {'content': f'{message_content}', 'tts': True, 'username': username}

    async with session.post(webhook_url, json=payload) as response:
        if response.status == 204:
            successful_messages += 1
            print(f"Message sent successfully. ({successful_messages}/{num_messages})")
            return True
        elif response.status == 429:
            print("Rate limited, retrying after 2 seconds...")
            await asyncio.sleep(2)
            return False
        else:
            print("Failed to send message. Retrying...")
            return False

async def webhook_spammer():
    webhook_url = input("Webhook URL: ")
    message_content = input("Message: ")
    username = input("Webhook username: ")
    num_messages = int(input("Number of messages to send: "))

    successful_messages = 0

    async with aiohttp.ClientSession() as session:
        while successful_messages < num_messages:
            try:
                success = await send_message(session, webhook_url, message_content, username, successful_messages, num_messages)
                if success:
                    successful_messages += 1
            except:
                print("An error occurred while sending the message. Retrying...")

    print("Total messages sent:", successful_messages)

asyncio.run(webhook_spammer())
