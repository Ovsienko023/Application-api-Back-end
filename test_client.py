import requests
import json


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
        "title": "Убрать в доме",
        "board": "Доска Дворника",
        "status": "Убрать",
        "description": "Необходимо всё убрать",
        "assignee": "Bob",
        "estimation": "4d"
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



#delete_board()
#create_board()
#delete_card()
#create_card()
update_card()


