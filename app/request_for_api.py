import requests
import json
url = 'http://127.0.0.1:5000/api'
headers = {"Content-type": "application/json","jsonrpc": "2.0", "method": "get_chats", "id": 1123 }
params = {'user_id' : 626}
method = {"method":"get_chats"}

data ={}
res = requests.post(url = url,data=json.dumps(params), json=json.dumps(method))
print(res)
print(res.text)
# CONTACTS_LIST = ['Profile1', 'Profile2', 'Profile3']
# result = {}
# result['status_code'] = '200 OK'
# result['mimetype'] = 'application/json'
# result['contacts'] = CONTACTS_LIST
# print((json.dumps(result)).replace(' ','as'))