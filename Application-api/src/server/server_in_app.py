import json
import time
import os
from logic.core_logic import ErrorApi, AuthenticationError


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

