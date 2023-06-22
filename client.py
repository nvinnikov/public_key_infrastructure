import requests

response = requests.get('https://localhost:5000', verify='root.crt')

print(response.text)
