import requests
import json


url = r'http://127.0.0.1:5000/api/v1/board/create'
#url = r'http://127.0.0.1:5000/api/v1/user/list'
#url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'


data = {
    "title": "Доска разработчика",
    "columns": [
        "ToDo",
        "InProgress",
        "Done"
]}


headers = {'UserName': 'Bob', 'UserSecret':'123'}


response = requests.post(url, json=data, headers=headers)
#print(response.content)
print(response.json())


# response = requests.get(url)
# print(response.json())



# r = requests.get(url, headers=headers)
# print(r.json())
