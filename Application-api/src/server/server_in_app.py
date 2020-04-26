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

