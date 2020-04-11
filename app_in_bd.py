import psycopg2
#from core_logic import Estimation

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
        with psycopg2.connect(**info_bd) as conn:
            with conn.cursor() as cursor:
                request = f"DELETE FROM Boards WHERE title = '{title}'"
                cursor.execute(request)   
                return cursor.statusmessage
    if tabl_name == 'card':
        board = data['board']
        return delete_card(title, board)

def get_card(name_card, name_board):
    try:
        with psycopg2.connect(**info_bd) as conn:
            with conn.cursor() as cursor:
                request = f""" SELECT user_name, times, title,
                                board, status, description, assignee,
                                estimation, board_id, last_update_at, last_update_by
                                FROM Cards 
                                where title = '{name_card}'
                                AND board = '{name_board}'
                        """
                cursor.execute(request)
                records = cursor.fetchall()
                for typles in records:
                    (user_name, times, title, board,
                    status, description, assignee, estimation,
                    board_id, last_update_at, last_update_by) = typles
                    
                    card = dict()
                    card['user_name'] = user_name
                    card['times'] = times
                    card['title'] = title
                    card['board'] = board
                    card['status'] = status
                    card['description'] = description
                    card['assignee'] = assignee
                    card['estimation'] = estimation
                    card['board_id'] = board_id
                    card['last_update_at'] = last_update_at
                    card['last_update_by'] = last_update_by
        delete_card(title, board)
        return card
    except UnboundLocalError:
        return ''


def delete_card(title, board):
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            request = f"DELETE FROM Cards WHERE title = '{title}' and board = '{board}'"
            cursor.execute(request)
            return cursor.statusmessage


def is_board(board_name):
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            request = f"SELECT title FROM Boards where title = '{board_name}'"
            cursor.execute(request)
            status = cursor.statusmessage.split(' ')[1]
            if status == '0':
                return True
            else: 
                return False

def report(data):
    status = data['column']
    name_board = data['board']
    user = data['assignee']
    with psycopg2.connect(**info_bd) as conn:
        with conn.cursor() as cursor:
            request = f""" SELECT user_name, times, title,
                                board, status, description, assignee,
                                estimation, board_id, last_update_at, last_update_by
                                FROM Cards 
                                where assignee = '{user}'
                                AND status = '{status}'
                                AND board = '{name_board}'
                        """
            cursor.execute(request)
            records = cursor.fetchall()
            return records
            
    
