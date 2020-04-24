import json
import time
import os
from logic.core_logic import Board, Card, Estimation, ErrorApi, AuthenticationError, config_app
#from logic.app_in_bd import get_users, get_card, get_boards, delete, report


def client_wrapper(user_name, user_secret, commands, data=None):
    try:
        authentication(user_name, user_secret)
    except AuthenticationError:
        return 'Authentication Error'

    clss, command = commands.split('_')
    print(command)
    try:
        if command == 'report':
            lst_report = report(data)
            return pars_for_rep(lst_report)

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

        if commands == 'board_list':
            status = get_boards()
            return status
        
    except ErrorApi:
        return ''





