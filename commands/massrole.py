	import aiohttp
		import asyncio
			import json
				import sys
					success = 0
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
																			    rname = input("Role name? ")
																				    num_role = int(input("Number of roles? "))
																					    async def start_bot():
																						        async with aiohttp.ClientSession(headers=headers) as session:
																							            await create_roles(session)
																								            await session.close()
																									async def create_roles(session):
																										    print("Creating roles...")
																											    create_role_url = f'https://discord.com/api/v9/guilds/{guild_id}/roles'
																												    create_tasks = []
																													    max_retries = 3
																														    
																															    for i in range(num_role):
																																        
																																	        create_role_payload = {
																																		            'name': f'{rname}',
																																			            'color': 0xffffff,
																																				            'hoist': True,
																																					            'mentionable': True
																																						        }
																																							        
																																								        create_tasks.append(create_role_with_retries(session, create_role_url, create_role_payload, max_retries))
																																									    create_responses = await asyncio.gather(*create_tasks)
																																										async def create_role_with_retries(session, url, payload, max_retries):
																																											    retries = 0
																																												    while retries <= max_retries:
																																													        try:
																																														            response = await session.post(url, json=payload)
																																															            if response.status == 429:
																																																                print(f"Rate limited waiting 3 seconds... ({success}/{num_role})")
																																																	                await asyncio.sleep(3)
																																																		                retries += 1
																																																			            elif response.status == 200:
																																																				                print(f"Created {rname} sucessfully ({success}/{num_role})")
																																																					                success += 1
																																																						            else:
																																																							                print(f"Failed to create role, Error code:{response.status} ({success}/{num_role})")
																																																								                return response
																																																									                sys.exit(1)
																																																										        except Exception:
																																																											            retries += 1
																																																												        await asyncio.sleep(1)
																																																													        
																																																														    print(f"Request failed {max_retries} times, skipping...")
																																																															    return None
																																																																asyncio.run(start_bot())

