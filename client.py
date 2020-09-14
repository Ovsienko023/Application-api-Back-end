
import requests


login = 'Bob'
passsword = '123'

def create_board():
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    data = {
        "title": "Доска Дворника 2",
        "columns": [
            "Пойти",
            "Убрать",
            "Уйти"
    ] }
    response = requests.post(url, json=data, auth=(login, passsword))
    print(response.content)


def delete_board():
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Доска Дворника 2",
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def create_card():
    url = r'http://127.0.0.1:5000/api/v1/card/create'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 2",
        "status": "Пойти",
        "description": "Необходимо за весь карантин не поехать кукухой ",
        "assignee": "Mark",
        "estimation": "1m"
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def update_card():
    url = r'http://127.0.0.1:5000/api/v1/card/update'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 2",
        "assignee": "Karlos"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def delete_card():
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 2"
    }

    response = requests.post(url, json=data, headers=headers)
    print(response.content)


def report():
    url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}
    data = {
        "board": "Доска Дворника 2",
        "column": "Пойти",
        "assignee": "Karlos"
		    }
	response = requests.post(url, json=data, headers=headers)
    print(response.json())
    # url = 'http://ru.stackoverflow.com/search?q=question'
    # # Параметры запроса
    # params = {
    #     'tag': 'python',
    # }
    # # Ответ
    # r = requests.get(url=url, params=params)


def board_list():
    url = r'http://127.0.0.1:5000/api/v1/board/list'
    headers = {'UserName': 'Bob', 'UserSecret':'123'}

    response = requests.get(url, headers=headers)
    print(response.json())