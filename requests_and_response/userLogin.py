import requests


endpoint = "http://127.0.0.1:8000/api/users/login/"

res = requests.post(endpoint, json={'username': 'nishant@gmail.com', 'password': '12345'})

print(res.content)  