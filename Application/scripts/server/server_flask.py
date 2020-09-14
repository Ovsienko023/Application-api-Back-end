from flask import Flask, request
from functools import wraps
import sys
from scripts.logic.core_logic import ClientWrapper,ErrorApi, AuthenticationError

app = Flask(__name__)


def main(obj_client):
    try:
        obj_client.authen
    except AuthenticationError:
        return 'Authentication Error'

    try:
        status = obj_client.command_define()
        print(status)
        return status   
    except ErrorApi:
        return ''


def post_request(command):
    data = request.json
    headers = request.headers
    user_name = headers['UserName']
    user_secret =  headers['UserSecret']

    obj_answer = ClientWrapper(user_name, user_secret, command, data=data)
    answer = main(obj_answer)
    if answer == "Error" or answer == 'DELETE 0' or answer == '':
        return {"Error": "Value"}

    if answer == 'ok' or answer == 'INSERT 0 1' or answer == 'DELETE 1':
        return {"ok":True}
    
    if answer:
        return answer
    

def get_request(command):
    headers = request.headers
    user_name = headers['UserName']
    user_secret =  headers['UserSecret']
    print('!')
    obj_answer = ClientWrapper(user_name, user_secret, command)
    print(obj_answer)
    answer = main(obj_answer)
    return answer


def authorization(func):
    @wraps(func)
    def wrapper():
        a = func()
        data = request.authorization
        print(data)
        if data['username'] == 'Bob':
            return a
        return {"status": "error"}
    return wrapper



@app.route('/api/v1/user/list',  methods=['GET'])
@authorization
def user_list():
    """ GET all user """

    return ''


@app.route('/api/v1/board/create', methods=['POST'])
@authorization
def board_creat():
    """
    request: {
        "title":"Name_board",
        "columns":[names_cards]
    }
    response: {"ok": true}
    """

    return ''


@app.route('/api/v1/board/delete', methods=['DELETE'])
@authorization
def board_delete():
    """
    {"title": "Доска разработчика"}
    """

    return ''


@app.route('/api/v1/board/list',  methods=['GET'])
@authorization
def board_list():
    """ GET all board """

    return ''


@app.route('/api/v1/card/create', methods=['POST'])
@authorization
def card_create():
    """
    {
        "title": "Развернуть PostgreSQL",
        "board": "Доска Разработчика",
        "status": "ToDo",
        "description": "Необходимо развернуть базу данных PostgreSQL",
        "assignee": "Username",
        "estimation": "8h"
    }
    """

    return ''


@app.route('/api/v1/card/update', methods=['PUT'])
@authorization
def card_update():
    """
    {
        "title": "Развернуть PostgreSQL",
        "board": "Доска разработчика",
        "status": "Done"
    }
    """

    return ''


@app.route('/api/v1/card/delete', methods=['DELETE'])
@authorization
def card_delete():
    """
    {
    "title": "Развернуть PostgreSQL",
    "board": "Доска разработчика"
    }
    """

    return ''


@app.route('/api/v1/report/cards_by_column', methods=['GET'])
@authorization
def report():
    """ 
    {
        "board": "Доска разработчика",
        "column": "ToDo",
        "assignee": "Username"
    }
    """

    return ''
