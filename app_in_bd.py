import psycopg2


def get_users():
    users = {'users': []}

    with psycopg2.connect(dbname='my_data_base', user='ovsienko023', 
                            password='68471325', host='localhost') as conn:
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

    with psycopg2.connect(dbname='my_data_base', user='ovsienko023', 
                            password='68471325', host='localhost') as conn:
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
    
    with psycopg2.connect(dbname='my_data_base', user='ovsienko023', 
                            password='68471325', host='localhost') as conn:
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


print(get_users(), get_boards(), get_cards())



# users = {'users': []}
# boards = {'boards': []}
# cards = {'cards': []}


# with psycopg2.connect(dbname='my_data_base', user='ovsienko023', 
#                         password='68471325', host='localhost') as conn:
#     with conn.cursor() as cursor:
#         cursor.execute('SELECT * FROM Users')
#         records = cursor.fetchall()
#         for typles in records:
#             user_name, user_secret = typles
#             _ = dict()
#             _['user_name'] = user_name
#             _['user_secret'] = user_secret
#             users['users'].append(_)
            

#         cursor.execute('SELECT * FROM Boards')
#         records = cursor.fetchall()
#         for typles in records:
#             user_name, times, title, columns, board_id = typles
#             _ = dict()
#             _['user_name'] = user_name
#             _['times'] = times
#             _['title'] = title
#             _['columns'] = columns.split(',')
#             _['board_id'] = board_id
#             boards['boards'].append(_)
            

#         cursor.execute('SELECT * FROM Cards')
#         records = cursor.fetchall()
#         for typles in records:
#             user_name, times, title, board, status, description, assignee, estimation, board_id = typles
#             _ = dict()
#             _['user_name'] = user_name
#             _['times'] = times
#             _['title'] = title
#             _['board'] = board
#             _['status'] = status
#             _['description'] = description
#             _['assignee'] = assignee
#             _['estimation'] = estimation
#             _['board_id'] = board_id
#             cards['cards'].append(_)
