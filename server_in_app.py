import json
import time
from core_logic import Board, Card, ErrorApi
from app_in_bd import get_users, get_card, delete


def client_wrapper(user_name, user_secret, commands, data=None):
    clss, command = commands.split('_')
    print()
    print(command)
    try:
        if command == 'report':
            return report(data)

        if commands == 'user_list':
            return {"count" :len(get_users()['users']), 
                        "users": [{'username':i['user_name']} for i in get_users()['users']] }
        
        if command == 'create':
            obj = crete_class(data, clss, user_name)
            status = f'{obj.save_in_bd()}'
            return status

        if command == 'delete':
            status = str(delete(data, clss))
            return status
        
        if command == 'update':
            status = update_card(data, user_name)
            return status
    except ErrorApi:
        return ''


def crete_class(data, clss, user_name):
    data['user_name'] = user_name
    data['times'] = time.time()
    classes = {'board': Board, 'card': Card}
    new_cls = classes[clss]
    new_cls = new_cls.create_from_dict(data)
    return new_cls


def update_card(data, user_name):
    try:
        name_card = data['title']
        name_board = data['board']
        card = get_card(name_card, name_board)
        obj_card = Card.create_from_dict(card)
        obj_card = update_obj(data, obj_card, user_name)
        status = obj_card.save_in_bd()
        return status

    except ErrorApi:
        return ''


def update_obj(data, obj, user_name):
    update_list = ['status', 'description', 'assignee', 'estimation']
    
    for key in ['title', 'board']:
        if data.get(key): data.pop(key)
    for key in data:
        if key == 'status':
            obj.status = data[key]
        if key == 'description':
            obj.description = data[key]
        if key == 'assignee':
            obj.assignee = data[key]
        if key == 'estimation':
            obj.estimation = data[key]
        if key not in update_list:
            raise ErrorApi
    obj.last_update_by = user_name
    return obj
def report(data):
    '''return json with data cards in DB'''
    pass




