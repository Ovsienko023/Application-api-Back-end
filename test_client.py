import requests
import json


url = r'http://127.0.0.1:5000/api/v1/card/create'
#url = r'http://127.0.0.1:5000/api/v1/user/list'


data = {
    "title": "Доска разработчика",
}

headers = {'UserName': 'Bob', 'UserSecret':'38rhh2824r2b27'}


response = requests.post(url, json=data, headers=headers)
print(response.content)


# response = requests.get(url)
# print(response.json())



# r = requests.get(url, headers=headers)
# print(r.json())