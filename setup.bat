	@echo off
		title Installing requirements...
			REM Check if 'pip' is available in the system
				where pip > nul 2>&1
					if %errorlevel% neq 0 (
						    echo Error: 'pip' command not found. Make sure Python is installed and is added to the system PATH.
							    pause
								    exit /b 1
									)
										REM Install python packages from requirements.txt
											py -m pip install -r requirements.txt
												if %errorlevel% neq 0 (
													    echo Error: Failed to install Python packages. Check if the requirements.txt file is valid.
														    pause
															    exit /b 1
																)
																	REM Run the main.py script
																		py main.py
																			if %errorlevel% neq 1 (
																				    echo Error: Failed to run the main.py script. Check if the file 'main.py' exists.
																					    pause
																						    exit /b 1
																							)
																								echo Installation and execution completed successfully.
																									pause
																										exit /b 0

