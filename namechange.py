import requests

def update_name(name, token):
    url = "https://www.clubhouseapi.com/api/update_name"
    headers = {"Authorization": f"Token {token}"}
    data = {
        "name": name
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Name updated successfully!")
    else:
        print("Failed to update name. Error:", response.text)

name = input("Enter your desired name: ")
token = input("Enter your token: ")

try:
    update_name(name, token)
except Exception as e:
    print("An error occurred:", str(e))
