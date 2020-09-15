from flask import Flask, request
from functools import wraps
import sys
from scripts.logic.core_logic import Destributor, ErrorApi


app = Flask(__name__)


def authorization(func):
    @wraps(func)
    def wrapper():
        a = func()
        data = request.authorization
        if data['username'] == 'Bob':
            return a
        return {"status": "error", "info": "Authentication Error"}
    return wrapper


@app.route('/api/v1/user/list',  methods=['GET'])
@authorization
def user_list():
    """ GET all user """
    user_name = request.authorization['username']
    status = Destributor(user_name).user_list()
    return status


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
    data = request.json
    user_name = request.authorization['username']
    status = Destributor(user_name, data=data).board_creat()
    return status


@app.route('/api/v1/board/delete', methods=['DELETE'])
@authorization
def board_delete():
    """
    {"title": "Доска разработчика"}
    """
    user_name = request.authorization['username']
    data = request.args.get('title')
    status = Destributor(user_name, data=data).board_delete()
    return status


@app.route('/api/v1/board/list',  methods=['GET'])
@authorization
def board_list():
    """ GET all board """
    user_name = request.authorization['username']
    status = Destributor(user_name).board_list()
    print(status)
    return status


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
    data = request.json
    user_name = request.authorization['username']
    status = Destributor(user_name, data=data).card_create()
    return status


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
    data = request.json
    user_name = request.authorization['username']
    status = Destributor(user_name, data=data).card_update()
    return status


@app.route('/api/v1/card/delete', methods=['DELETE'])
@authorization
def card_delete():
    """
    {
    "title": "Развернуть PostgreSQL",
    "board": "Доска разработчика"
    }
    """
    user_name = request.authorization['username']
    data = dict(request.args)
    status = Destributor(user_name, data=data).card_delete()
    return status
 

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
    data = dict(request.args)
    user_name = request.authorization['username']
    status = Destributor(user_name, data=data).report()
    return status

