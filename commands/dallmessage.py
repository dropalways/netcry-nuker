import requests
import time
import datetime


def questions():
    with open("token.txt", "r") as file:
        token = file.readline().strip()

    if token == "":
        print("Empty token in token.txt")
        print("Ignore the error below i dont know how to fix it if you know how to fix it create a pull request")
        return

    selfbot = input("Selfbot? [y|n] ")
    if selfbot == "y":
        headers = {'Authorization': f'{token}',
                   'Content-Type': 'application/json'}
    elif selfbot == "n":
        headers = {'Authorization': f'Bot {token}',
                   'Content-Type': 'application/json'}
    else:
        print("Invalid answer")
        return None, None
    channel_id = input("What channel do you wanna delete your messages from ")
    return channel_id, headers


def get_messages(channel_id, user_id, headers):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    params = {
        "limit": 100
    }
    messages = []

    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if len(data) == 0:
                break
            for message in data:
                if message['author']['id'] == user_id:
                    messages.append(message)
            if len(data) < 100:
                break
            params["before"] = data[-1]["id"]
        elif response.status_code == 429:
            print("Rate limited. Waiting 10 seconds...")
            time.sleep(10)
        else:
            print("Failed to retrieve messages.")
            break

    return messages


def delete_messages(channel_id, messages, headers):
    success_count = 0
    for message in messages:
        url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message['id']}"
        response = requests.delete(url, headers=headers)
        if response.status_code == 204:
            timestamp = datetime.datetime.strptime(
                message['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
            formatted_timestamp = timestamp.strftime("%H:%M:%S %d/%m/%y")
            print(
                f"Deleted message: {message['content']} (Sent at: {formatted_timestamp})")
            success_count += 1
        elif response.status_code == 429:
            print("Rate limited. Waiting 3 seconds...")
            time.sleep(3)
            continue
        else:
            print(f"Failed to delete message with ID: {message['id']}")

    return success_count


def main():
    channel_id, headers = questions()
    if channel_id is None or headers is None:
        return

    response = requests.get(
        "https://discord.com/api/v9/users/@me", headers=headers)
    data = response.json()
    user_id = data['id']

    messages = get_messages(channel_id, user_id, headers)
    if len(messages) == 0:
        print("No messages found.")
    else:
        print(f"Found {len(messages)} messages")
        amount = int(input("Enter the amount of messages to delete: "))
        deleted_count = delete_messages(channel_id, messages[:amount], headers)
        print(f"Deleted {deleted_count} messages")


if __name__ == "__main__":
    main()
