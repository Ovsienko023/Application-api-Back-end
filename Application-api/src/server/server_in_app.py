import json
import time
import os
from logic.core_logic import ErrorApi, AuthenticationError # Board, Card, Estimation, , config_app
#from logic.app_in_bd import get_users, get_card, get_boards, delete, report


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


def command_define(self):
        clss, command = self.commands.split('_')
        if command == 'report':
            lst_report = report(data)
            return pars_for_rep(lst_report)

        if command == 'create':
            obj = ClientWrapper.crete_class(self.data, clss, self.user_name)
            status = f'{obj.save_in_bd()}'
            return status
        #!!!
        if command == 'delete':
            status = str(delete(self.data, clss))
            return status
        
        if command == 'update':
            status = DataInJson.update_card(self.data, self.user_name)
            return status

        if self.commands == 'user_list':
            return {"count" :len(DataInDB.get_users()['users']), 
                        "users": [{'username':i['user_name']} for i in DataInDB.get_users()['users']] }
        
        if self.commands == 'board_list':
            status = DataInDB.get_boards()
            return status


