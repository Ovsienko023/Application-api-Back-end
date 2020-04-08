from flask import Flask, request
from server_in_app import client_wrapper

app = Flask(__name__)


users = {
    #'Name_user': 'token'
    'Bob': '38rhh2824r2b27',
}


def post_request(command):
    data = request.json
    answer = client_wrapper(command, data=data)
    if answer:
        return {"ok":True}


@app.route('/api/v1/info')
def info():
    with open('read_me.txt') as r:
        message = r.read()
    return message


@app.route('/api/v1/user/list')
def user_list():
    """ GET all user """

    command = 'user_list'
    return client_wrapper(command)


@app.route('/api/v1/board/create', methods=['POST'])
def board_creat():
    """
    request: {
        "title":"Name_board",
        "columns":[names_cards]
    }
    response: {"ok": true}
    """
    command = 'board_creat'
    return post_request(command)


@app.route('/api/v1/board/delete', methods=['POST'])
def board_delete():
    """
    {"title": "Доска разработчика"}
    """

    command = 'board_delete'
    return post_request(command)


@app.route('/api/v1/board/list')
def board_list():
    """ GET all board """

    command = 'board_list'
    return client_wrapper(command)


@app.route('/api/v1/card/create', methods=['POST'])
def card_create():
    """
    {
        "title": "Развернуть PostgreSQL",
        "board": "Доска разработчика",
        "status": "ToDo",
        "description": "Необходимо развернуть базу данных PostgreSQL",
        "assignee": "Username",
        "estimation": "8h"
    }
    """

    command = 'card_create'
    return post_request(command)


@app.route('/api/v1/card/update', methods=['POST'])
def card_update():
    """
    {
        "title": "Развернуть PostgreSQL",
        "board": "Доска разработчика",
        "status": "Done"
    }
    """

    command = 'card_update'
    return post_request(command)


@app.route('/api/v1//report/cards_by_column')
def report():
    """ 
    {
        "board": "Доска разработчика",
        "column": "ToDo",
        "assignee": "Username"
    }
    """

    command = 'report'
    return client_wrapper(command)


app.run()
