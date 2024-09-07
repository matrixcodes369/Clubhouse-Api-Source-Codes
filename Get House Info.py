import requests
import re

profile_URL = input('Enter House link or ( press q to quit ): ')

if profile_URL.lower() == 'q':
    pass
else:
    club_id = re.search('/house/(.+)$', profile_URL).group(1)
    json_data = {'social_club_slug': club_id}
    token = 'YOUR TOKEN HERE'
    headers = {'Authorization': f'Token {token}'}
    try:
        url = 'https://www.clubhouseapi.com:443/api/get_social_club'
        response = requests.post(url, headers=headers, json=json_data)
        print(response)
        data = response.json()
        print(data)
        if 'social_club' in data:
            social_club_id = data['social_club']['social_club_id']
            print(f"{social_club_id}")
        else:
            print("House information not found.")

    except Exception as e:
        print(f'Error occurred: {e}')
