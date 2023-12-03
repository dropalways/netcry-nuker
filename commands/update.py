	import shutil
		import tempfile
			import requests
				import sys
					import time
						import os
							import subprocess
								def update():
									    response = requests.get("https://raw.githubusercontent.com/dropalways/netcry-nuker/main/version.txt")
										    with open("version.txt", "r") as file:
											        localversion = file.readline().strip()
												    if localversion < response.text:
													        print(f"Local version is: {localversion} Latest: {response.text}")
														        response = requests.get("https://github.com/dropalways/netcry-nuker/archive/refs/heads/main.zip")
															        if response.status_code == 200:
																            print("Downloaded latest release")
																	            temp_dir = tempfile.mkdtemp()
																		            update_zip_path = os.path.join(temp_dir, 'update.zip')
																			            with open(update_zip_path, 'wb') as update_file:
																				                update_file.write(response.content)
																					            shutil.unpack_archive(update_zip_path, extract_dir=temp_dir)
																						            latest_files_dir = os.path.join(temp_dir, 'netcry-nuker-main')
																							            shutil.copytree(latest_files_dir, ".", dirs_exist_ok=True)
																								            print("Update installed successfully.")
																									            subprocess.run(f"start cmd /k python main.py", shell=True)
																										            sys.exit(0)
																											        else:
																												            print("Failed to download latest release")
																													    elif response.status_code != 200:
																														        print(f"Couldn't update. Error code: {response.status_code}")
																															update()

