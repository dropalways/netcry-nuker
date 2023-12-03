	import asyncio
		import aiohttp
			import time
				import datetime
					async def questions():
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
																						    channel_id = input(
																							        "What channel ID do you wanna delete your messages from: ")
																								    return channel_id, headers
																									async def get_messages(channel_id, user_id, headers):
																										    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
																											    params = {
																												        "limit": 100
																													    }
																														    messages = []
																															    while True:
																																        async with aiohttp.ClientSession() as session:
																																	            async with session.get(url, headers=headers, params=params) as response:
																																		                if response.status == 200:
																																			                    data = await response.json()
																																				                    if len(data) == 0:
																																					                        break
																																						                    for message in data:
																																							                        if message['author']['id'] == user_id:
																																								                            messages.append(message)
																																									                    if len(data) < 100:
																																										                        break
																																											                    params["before"] = data[-1]["id"]
																																												                elif response.status == 429:
																																													                    print("Rate limited. Waiting 10 seconds...")
																																														                    await asyncio.sleep(10)
																																															                else:
																																																                    print("Failed to retrieve messages.")
																																																	                    break
																																																		    return messages
																																																			async def delete_messages(channel_id, messages, headers):
																																																				    success_count = 0
																																																					    async with aiohttp.ClientSession() as session:
																																																						        for message in messages:
																																																							            url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message['id']}"
																																																								            retry_count = 0
																																																									            while retry_count < 3:
																																																										                async with session.delete(url, headers=headers) as response:
																																																											                    if response.status == 204:
																																																												                        timestamp = datetime.datetime.strptime(
																																																													                            message['timestamp'], "%Y-%m-%dT%H:%M:%S.%f%z")
																																																														                        formatted_timestamp = timestamp.strftime(
																																																															                            "%H:%M:%S %d/%m/%y")
																																																																                        print(
																																																																	                            f"Deleted message: {message['content']} (Sent at: {formatted_timestamp})")
																																																																		                        await asyncio.sleep(0.3)
																																																																			                        success_count += 1
																																																																				                        break
																																																																					                    elif response.status == 429:
																																																																						                        print("Rate limited. Waiting 3 seconds...")
																																																																							                        await asyncio.sleep(3)
																																																																								                        retry_count += 1
																																																																									                    else:
																																																																										                        print(
																																																																											                            f"Failed to delete message with ID: {message['id']}")
																																																																												                        break
																																																																													    return success_count
																																																																														async def main():
																																																																															    channel_id, headers = await questions()
																																																																																    if channel_id is None or headers is None:
																																																																																	        return
																																																																																		    async with aiohttp.ClientSession() as session:
																																																																																			        async with session.get("https://discord.com/api/v9/users/@me", headers=headers) as response:
																																																																																				            data = await response.json()
																																																																																					            user_id = data['id']
																																																																																						    messages = await get_messages(channel_id, user_id, headers)
																																																																																							    if len(messages) == 0:
																																																																																								        print("No messages found.")
																																																																																									    else:
																																																																																										        print(f"Found {len(messages)} messages")
																																																																																											        amount = input("Enter the amount of messages to delete (num/all): ")
																																																																																												        if amount != 'all':
																																																																																													            amount = int(amount)
																																																																																														        else:
																																																																																															            print("Deleting all messages...")
																																																																																																            amount = len(messages)
																																																																																																	        deleted_count = await delete_messages(channel_id, messages[:amount], headers)
																																																																																																		        print(f"Deleted {deleted_count} messages")
																																																																																																			if __name__ == "__main__":
																																																																																																				    asyncio.run(main())

