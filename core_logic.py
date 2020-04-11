import time
import psycopg2
from app_in_bd import info_bd, is_board

class Board:
    required = ['user_name', 'title', 'columns', ]

    def __init__(self, user_name, title, columns):
        self.times = time.time()
        self.user_name = user_name
        self.title = title
        self.columns = self.valid_columns(columns)
        self.board_id = int(str(hash(self.times))[:5])


    def valid_columns(self, columns):
        if isinstance(columns, list):
            columns = ','.join(columns)
            return columns
        else:
            raise ErrorApi

    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)


    def save_in_bd(self):
        if is_board(self.title):
            
            with psycopg2.connect(** info_bd) as conn:
                with conn.cursor() as cursor:
                    request = f"""INSERT INTO Boards (user_name, times, title, columns, board_id)
                                VALUES ('{self.user_name}', '{self.times}',
                                '{self.title}', '{self.columns}', {self.board_id})
                    """
                    cursor.execute(request)
                    return cursor.statusmessage
        else:
            raise ErrorApi


class Card:
    required = ['user_name', 'title', 'board', 
                'status', 'description', 'assignee', 
                'estimation', 'times']

    def __init__(self, user_name, title, board, status, description, assignee, estimation, times):
        self.times = times
        self.user_name = user_name
        self.title = title
        self.board = board
        self.status = status
        self.description = description
        self.assignee = assignee
        self.estimation = estimation
        self.board_id = self.get_board_id()
        self.last_update_at = time.time()
        self.last_update_by = user_name

    @classmethod
    def create_from_dict(cls, data):
        try:
            parameters = [data[parameter] for parameter in cls.required]
            return cls(*parameters)
        except TypeError:
            raise ErrorApi
        


    def get_board_id(self):
        try:
            with psycopg2.connect(** info_bd) as conn:
                with conn.cursor() as cursor:
                    print(self.board)
                    request = "SELECT board_id FROM Boards where title ='{}'".format(self.board)
                    cursor.execute(request)
                    records = cursor.fetchall()
                    print(records)
                    return records[0][0]
        except IndexError:
            raise ErrorApi
    
    def save_in_bd(self):
        with psycopg2.connect(** info_bd) as conn:
            with conn.cursor() as cursor:
                request = f"""INSERT INTO Cards (user_name, times, title, board, status,
                                                    description, assignee, estimation, board_id, 
                                                    last_update_at, last_update_by)
                            VALUES ('{self.user_name}', '{self.times}',
                            '{self.title}', '{self.board}', '{self.status}',
                            '{self.description}', '{self.assignee}', '{self.estimation}',
                             {self.board_id}, '{self.last_update_at}', '{self.last_update_by}')
                """
                cursor.execute(request)
                return cursor.statusmessage
        print("отправленно")



class Estimation:
    def __init__(self, num, cal):
        self.pnum = num
        self.cal = cal
        if self.cal == 'd':
            self.num = num * 8 
        if self.cal == 'w':
            self.num = num * 40
        if self.cal == 'm':
            self.num = num * 160 
        if self.cal == 'h':
            self.num = num
    
    def __add__(self, obj):
        if 7 < (self.num + obj.num) < 40:
            a = 1
            b = (self.num + obj.num) - 8
            while True:
                if b > 7:
                    a += 1
                    b -= 8
                else:
                    return f'{a}d{b}h'
                    
        if 39 < (self.num + obj.num) < 160:
            a = 1
            b = 0
            c = (self.num + obj.num) - 40
            while True:
                if c > 7:
                    b += 1
                    c -= 8
                    if b > 4:
                        a += 1
                        b -= 5
                else:
                    return f'{a}w{b}d{c}h'
                
        if (self.num + obj.num) >= 160:
            a = 1
            b = 0
            c = 0
            d = (self.num + obj.num) - 160
            while True:
                if d > 7:
                    c += 1
                    d -= 8
                    if c > 4:
                        b += 1
                        c -= 5
                        if b > 3:
                            a += 1
                            b -= 4
                else:
                    return f'{a}m{b}w{c}d{d}h'
        
    def __str__(self):
        return str(self.pnum) + self.cal

    def __repr__(self):
        return str(self.pnum) + self.cal



class ErrorApi(Exception):
    pass