import requests
import json


url = r'http://127.0.0.1:5000/api/v1/card/create'
#url = r'http://127.0.0.1:5000/api/v1/user/list'
#url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'


data = {
    "title": "Развернуть PostgreSQL",
    "board": "Доска Разработчика",
    "status": "ToDo",
    "description": "Необходимо развернуть базу данных PostgreSQL",
    "assignee": "Username",
    "estimation": "8h"
}


headers = {'UserName': 'Bob', 'UserSecret':'123'}


response = requests.post(url, json=data, headers=headers)
print(response.content)


# response = requests.get(url)
# print(response.json())



# r = requests.get(url, headers=headers)
# print(r.json())