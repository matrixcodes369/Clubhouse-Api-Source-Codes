import requests

def get_user_profile():
    token = input("Please enter your Clubhouse API token: ")
    url = "https://www.clubhouseapi.com/api/me"
    headers = {'Authorization': f'Token {token}'}
    data = {
    "return_blocked_ids": True,
    "timezone_identifier": "Asia/Tehran",
    "return_following_ids": True
}
    try:
        response = requests.post(url, headers=headers, json= data)
        response.raise_for_status()
        data = response.json()
        print(data)
        user_data = data.get('user_profile')
        user_id = user_data.get('user_id')
        name = user_data.get('name')
        photo_url = user_data.get('photo_url')
        username = user_data.get('username')
        following_ids = data['following_ids']
        email = data.get('email')
        phone_number = data.get('phone_number')
        return user_id, name, photo_url, username, following_ids, email, phone_number
    except requests.exceptions.HTTPError as err:
        print(f"An HTTP error occurred: {err}")
        return None, None, None, None, None, None, None


if __name__ == "__main__":
    user_id, name, photo_url, username, following_ids, email, phone_number = get_user_profile()
    if user_id:
        print(f"User ID: {user_id}")
        print(f"Name: {name}")
        print(f"Photo URL: {photo_url}")
        print(f"Username: {username}")
        print(f"Following IDs: {following_ids}")
        print(f"Email: {email}")
        print(f"Phone Number: {phone_number}")
    else:
        print("Failed to retrieve user profile data.")
