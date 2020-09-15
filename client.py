
import requests
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

login = 'Bob'
passsword = '123'
hash_ = generate_password_hash(passsword) # Для записи пользователя
def user_list():
    url = r'http://127.0.0.1:5000/api/v1/user/list'
    response = requests.get(url, auth=(login, passsword))
    print(response.json())



def create_board():
    url = r'http://127.0.0.1:5000/api/v1/board/create'
    data = {
        "title": "Доска Дворника 1",
        "columns": [
            "Пойти",
            "Убрать",
            "Уйти"
    ] }
    response = requests.post(url, json=data, auth=(login, passsword))
    print(response.content)



def delete_board():
    url = r'http://127.0.0.1:5000/api/v1/board/delete'
    data = {
        "title": "Доска Дворника 1",
    }

    response = requests.delete(url, params=data, auth=(login, passsword))
    print(response.json())


def create_card():
    url = r'http://127.0.0.1:5000/api/v1/card/create'
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 1",
        "status": "Пойти",
        "description": "Необходимо за весь карантин не поехать кукухой ",
        "assignee": "Mark",
        "estimation": "1m"
    }
    response = requests.post(url, json=data, auth=(login, passsword))
    print(response.json())


def update_card():
    url = r'http://127.0.0.1:5000/api/v1/card/update'
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 1",
        "assignee": "Karlos"
    }

    response = requests.put(url, json=data, auth=(login, passsword))
    print(response.content)


def delete_card():
    url = r'http://127.0.0.1:5000/api/v1/card/delete'
    data = {
        "title": "Painter_",
        "board": "Доска Дворника 1"
    }

    response = requests.delete(url, params=data, auth=(login, passsword))
    print(response.content)


def report():
    url = r'http://127.0.0.1:5000/api/v1/report/cards_by_column'
    data = {
        "board": "Доска Дворника 1",
        "column": "Пойти",
        "assignee": "Karlos"
		    }
    response = requests.get(url, params=data, auth=(login, passsword))
    print(response.json())


def board_list():
    url = r'http://127.0.0.1:5000/api/v1/board/list'
    response = requests.get(url, auth=(login, passsword))
    print(response.json())

# user_list()
# board_list()
# create_board()
delete_board()
# create_card()
# update_card()
# delete_card()
# report()