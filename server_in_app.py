import json
from core_logic import Board, Card
from app_in_bd import get_users

def client_wrapper(user_name, user_secret, commands, data=None):
    clss, command = commands.split('_')
    print(user_name, user_secret, data, commands)
    print()
    print(command)
    if command == 'report':
        return report(data)

    if commands == 'user_list':
        return {"count" :len(get_users()['users']), 
                    "users": [{'username':i['user_name']} for i in get_users()['users']] }
    
    if command == 'creat':
        obj = crete_class(data, clss, user_name)
        return f'{obj.save_in_bd()}'

    return {}


def crete_class(data, clss, user_name):
    data['user_name'] = user_name
    classes = {'board': Board, 'card': Card}
    new_cls = classes[clss]
    new_cls = new_cls.create_from_dict(data)
    return new_cls

def report(data):
    '''return json with data cards in DB'''
    pass




 # #-----СОЗДАНИЕ КЛАССА ЕСЛИ ПРИХОДИТ create
    # obj = crete_class(data, clss, user_name)
    # print(obj.board_id)
    # # obj -->> app_in_bd 