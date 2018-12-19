import requests

url = 'https://httpbin.org/post'
files = {'file': open('yoda.jpeg', 'rb')}

r = requests.post(url, files=files)

print(r.text)
