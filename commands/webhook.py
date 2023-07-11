import asyncio
import aiohttp
import time

async def send_webhook_message(webhook_url, payload):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(webhook_url, json=payload) as response:
                if response.status == 204:
                    print("Message sent successfully")
                else:
                    print("Failed to send message")
        except aiohttp.ClientError as e:
            print(f"An error occurred: {str(e)}")

async def send_multiple_messages(webhook_url, embed_payload, text_payloads):
    tasks = []
    async with aiohttp.ClientSession() as session:
        tasks.append(send_webhook_message(webhook_url, embed_payload))
        count = 0
        for text_payload in text_payloads:
            tasks.append(send_webhook_message(webhook_url, text_payload))
            count += 1
            if count % 3 == 0:
                await asyncio.sleep(0.8)  
        await asyncio.gather(*tasks)

try:
    webhook_url = input("Enter Webhook URL: ")
    image_url = "https://cdn.discordapp.com/attachments/1125825818552172627/1127217004563152926/20230614_165818.jpg"
    footer_text = "Powered by NetCry"

    embed_message = input("Enter the message for the embed: ")
    text_message = input("Enter the message for the regular text messages: ")
    count = int(input("Enter the number of messages to send: "))

    embed_payload = {
        "embeds": [{
            "description": embed_message,
            "image": {
                "url": image_url
            },
            "footer": {
                "text": footer_text
            }
        }]
    }

    text_payloads = []
    for _ in range(count):
        text_payloads.append({
            "content": text_message
        })

    loop = asyncio.get_event_loop()
    start_time = time.time()
    loop.run_until_complete(send_multiple_messages(webhook_url, embed_payload, text_payloads))
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")

except ValueError:
    print("Invalid input. Please enter a valid number for the count.")
except KeyboardInterrupt:
    print("Operation interrupted by the user.")
except Exception as e:
    print(f"An error occurred: {str(e)}")


