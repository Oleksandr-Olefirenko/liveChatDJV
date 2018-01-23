import requests

url = 'http://127.0.0.1:8080/auth/users/create/'
url_token = 'http://127.0.0.1:8080/auth/token/create/'

rsp = requests.post(url, json={'username': 'AlekS', 'password': 'Tyler@28', 'email': 'smth@mail.com'})
print(rsp.content)
print(rsp.status_code)

rsp_token = requests.post(url_token, json={'username': 'AlekS', 'password': 'Tyler@28'})
print(rsp_token.content)
print(rsp_token.status_code)