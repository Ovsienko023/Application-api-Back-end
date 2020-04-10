import psycopg2


info_bd = {'dbname': 'my_data_base', 'user': 'ovsienko023', 
                            'password': '68471325', 'host':'localhost'}


def get_users():
    users = {'users': []}

    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM Users')
            records = cursor.fetchall()
            for typles in records:
                user_name, user_secret = typles
                _ = dict()
                _['user_name'] = user_name
                _['user_secret'] = user_secret
                users['users'].append(_)
    return users


def get_boards():
    boards = {'boards': []}

    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM Boards')
            records = cursor.fetchall()
            for typles in records:
                user_name, times, title, columns, board_id = typles
                _ = dict()
                _['user_name'] = user_name
                _['times'] = times
                _['title'] = title
                _['columns'] = columns.split(',')
                _['board_id'] = board_id
                boards['boards'].append(_)
    return boards


def get_cards():
    cards = {'cards': []}
    
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM Cards')
            records = cursor.fetchall()
            for typles in records:
                user_name, times, title, board, status, description, assignee, estimation, board_id = typles
                _ = dict()
                _['user_name'] = user_name
                _['times'] = times
                _['title'] = title
                _['board'] = board
                _['status'] = status
                _['description'] = description
                _['assignee'] = assignee
                _['estimation'] = estimation
                _['board_id'] = board_id
                cards['cards'].append(_)
    return cards


def delete(data, tabl_name):
    title = data['title']
    if tabl_name == 'board':
        tabl_name = 'Boards'
    if tabl_name == 'card':
        tabl_name = 'Cards'

    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            request = f"DELETE FROM {tabl_name} WHERE title = '{title}'"
            cursor.execute(request)   
            return cursor.statusmessage
    