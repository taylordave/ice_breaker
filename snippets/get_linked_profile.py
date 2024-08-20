from dotenv import load_dotenv
load_dotenv()
import os

import requests

headers = {'Authorization': 'Bearer ' + os.getenv('PROXYCURL_API_KEY')}
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

params = {
    'linkedin_profile_url': 'https://linkedin.com/in/dave-taylor-86b7105/',
}

response = requests.get(api_endpoint,
                        params=params,
                        headers=headers)

print(response.json())
