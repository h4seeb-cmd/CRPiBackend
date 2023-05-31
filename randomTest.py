import requests
import json

url = "http://127.0.0.1:8086/api/binary/post"
headers = {'Content-Type': 'application/json'}

data = {
    'tag': 'your_tag_here'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print("Request failed with status code:", response.status_code)
