	import requests
		import time
			import concurrent.futures
				from sys import exit
					def ball():
						    with open("token.txt", "r") as file:
							        token = file.readline().strip()
								    headers = {'Authorization': f'Bot {token}'}
									    if token == "":
										        print("Empty token")
											        print("Ignore the error below; I don't know how to fix it. If you know how to fix it, create a pull request")
												    elif token == "single token here":
													        print("You haven't edited the file 'token.txt'.")
														        print("Ignore the error below; I don't know how to fix it. If you know how to fix it, create a pull request")
															    else:
																        print("This will only work with bot tokens")
																	        try:
																		            massban(token, headers)
																			        except KeyboardInterrupt:
																				            exit()
																					def massban(token, headers):
																						    guild_id = input("Enter the target guild id: ")
																							    whitelist = input(
																								        "Do you want to whitelist anyone from getting banned? (y/n): ")
																									    whitelistids = []
																										    if whitelist.lower() == "y":
																											        while True:
																												            user_id = input(
																													                "Enter a user id you want to whitelist (or enter nothing to stop): ")
																														            if not user_id:
																															                break
																																            whitelistids.append(user_id)
																																	    else:
																																		        pass
																																			    hm = requests.get(
																																				        f'https://discord.com/api/v9/guilds/{guild_id}/members?limit=1000', headers=headers)
																																					    if hm.status_code == 200:
																																						        members = hm.json()
																																							        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
																																								            ban_tasks = [executor.submit(
																																									                ban_member, guild_id, member['user']['id'], token, headers, whitelistids) for member in members]
																																										            concurrent.futures.wait(ban_tasks)
																																											    else:
																																												        print(f"Error code: {hm.status_code}")
																																													def ban_member(guild_id, user_id, token, headers, whitelistids):
																																														    if user_id in whitelistids:
																																															        print(f"User {user_id} is whitelisted and won't be banned.")
																																																        return
																																																	    response = requests.put(
																																																		        f'https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}', headers=headers)
																																																			    if response.status_code == 204:
																																																				        print(f"Banned {user_id}")
																																																					    elif response.status_code == 429:
																																																						        print(f"Rate limited, waiting 0.7 seconds... {response.status_code}")
																																																							        time.sleep(0.7)
																																																								    else:
																																																									        print(f"Failed to ban {user_id} {response.status_code}")
																																																										ball()

