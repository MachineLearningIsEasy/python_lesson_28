import requests
import os

SERVER ='http://127.0.0.1:8000/'
PAGE = 'api-tag/tag/'
tag = '1'

response = requests.get(os.path.join(SERVER, PAGE, tag))

print(response.status_code, response.text)