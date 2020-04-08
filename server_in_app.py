import json


def client_wrapper(command, data=None):
    user_list = {
        "count": 2,
        "users": [{"username": "Петя",},
                {"username": "Вася",}]
    }
    if data == None:
        return user_list
    print(data, command)
    return True
