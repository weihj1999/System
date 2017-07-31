import requests

headers = {'Content-Type': 'application/json'}
data = open('data/auth.json','rb')
url = 'https://iam.eu-de.otc.t-systems.com:443/v3/auth/tokens'

r = requests.post(url, data,headers)
print r.headers.get('X-Subject-Token')
