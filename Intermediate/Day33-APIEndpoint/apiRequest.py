import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response = requests.get(url="https://api.kanye.rest")

response.raise_for_status()

data = response.json()
# longitude = data['iss_position']['longitude']
print(data)
# print(longitude)
