import json
from core_logic import Board, Card

def client_wrapper(user_name, user_secret, commands, data=None):
    clss, command = commands.split('_')
    # user_list = {
    #     "count": 2,
    #     "users": [{"username": "Петя",},
    #             {"username": "Вася",}]
    # }
    # if data == None:
    #     return user_list
    print(user_name, user_secret, data, commands)
    data['user_name'] = user_name
    obj = crete_class(data, clss)
    print(obj.board_id)
    # obj -->> app_in_bd 
    return True


def crete_class(data, clss):
    classes = {'board': Board, 'card': Card}
    new_cls = classes[clss]
    new_cls = new_cls.create_from_dict(data)
    return new_cls