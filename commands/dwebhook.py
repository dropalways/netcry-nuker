import requests

def delet():
    dwebhook = input("Webhook url: ")
    response = requests.delete(dwebhook)
    if response.status_code == 204:
        print("Deleted webhook successfully!")
    elif response.status_code == 404:
        print("Error: Webhook doesn't exist")
    else:
        print(f"Error occurred: {response.status_code}")
        
delet()
