import requests

response = requests.get('https://localhost:5000', verify='cert.pem', headers={'Host': 'localhost'})
print(response.text)
