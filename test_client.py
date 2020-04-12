import requests
import json
import pprint

def create_board():
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Доска Дворника",
        "columns": [
            "Пойти",
            "Убрать",
            "Уйти"
    ] }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def delete_board():
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Доска Дворника",
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def delete_card():
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Развернуть PostgreSQL",
        "board": "Доска Разработчика"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def create_card():
    url = r'http://127.0.0.1:5000/api/v1/card/create'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Кукуха",
        "board": "Доска Дизайнера",
        "status": "ToDo",
        "description": "Необходимо за весь карантин не поехать кукухой ",
        "assignee": "Mark",
        "estimation": "1m"
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def update_card():
    url = r'http://127.0.0.1:5000/api/v1/card/update'
    headers = {'UserName': 'Karl', 'UserSecret':'289'}
    data = {
        "title": "Убрать в доме",
        "board": "Доска Дворника",
        "assignee": "Karl"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def report():
    url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "board": "Доска Дизайнера",
        "column": "ToDo",
        "assignee": "Mark"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.json())


def board_list():
    url = r'http://127.0.0.1:5000/api/v1/board/list'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}


    response = requests.get(url, headers=headers)
    print(response.content)
    




#delete_board()
#create_board()
#delete_card()
#create_card()
#update_card()
#report()
board_list()
