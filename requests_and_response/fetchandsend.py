import requests

endpoint = "http://127.0.0.1:8000/api/users/register/" 

req = requests.post(endpoint, json={'username': 'new_user',
                                    'email':'new.user@gmail.com',
                                     'password': '12345'})

print(req.content)

