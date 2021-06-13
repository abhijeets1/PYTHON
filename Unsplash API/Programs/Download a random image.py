import requests
from mypackage import config

url = 'https://api.unsplash.com/photos/random?topics=wallpapers&orientation=landscape&client_id='

url += config.accesskey

response = requests.get(url)
data = response.json()

imageid = data['id']
imagelink = data['urls']['regular']

with open('images/' + imageid + '.jpg', '+wb') as file:
	file.write(requests.get(imagelink).content)