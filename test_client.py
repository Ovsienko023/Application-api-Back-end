import requests
import json


#url = r'http://127.0.0.1:5000/api/v1/board/delete'
#url = r'http://127.0.0.1:5000/api/v1/user/list'
#url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'


# data = {
#     "title": "Доска Разработчика",
# }


# headers = {'UserName': 'Bob', 'UserSecret':'123'}


# response = requests.post(url, json=data, headers=headers)
# print(response.content)
# #print(response.json())


# response = requests.get(url)
# print(response.json())

# r = requests.get(url, headers=headers)
# print(r.json())


def create_board():
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Доска Дизайнера",
        "columns": [
            "ToDo",
            "InProgress",
            "Done"
] }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def delete_board():
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Доска Разработчика",
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def delete_card():
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "flex",
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


# create_board()
#delete_board()
delete_card()


