import json


users = {
    #'Name_user': 'token'
    'Bob': '38rhh2824r2b27',
}


def client_wrapper(user_name, user_secret, command, data=None):
    user_list = {
        "count": 2,
        "users": [{"username": "Петя",},
                {"username": "Вася",}]
    }
    if data == None:
        return user_list
    print(user_name, user_secret, data, command)
    return True
