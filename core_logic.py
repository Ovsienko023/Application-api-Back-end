import time
import psycopg2
from app_in_bd import info_bd, is_board, is_card



class Estimation:
    def __init__(self, num, cal):
        self.pnum = num
        self.cal = cal
        if self.cal == 'd':
            self.num = int(num) * 8 
        if self.cal == 'w':
            self.num = int(num) * 40
        if self.cal == 'm':
            self.num = int(num) * 160 
        if self.cal == 'h':
            self.num = int(num)
        self.lst_obj = []

    
    def __add__(self, obj):
        sum_str = self.num + obj.num 
        return Estimation(sum_str, 'h')
   
        
    def pars(self):
        sum_str = self.logic()
        index = sum_str.find('0')
        while index != -1:
            sum_str = sum_str[:index] + sum_str[(index + 2):]
            index = sum_str.find('0')
        return sum_str
        

    def __str__(self):
        return str(self.num) + 'h'


    def __repr__(self):
        return str(self.pnum) + 'h'

    
    def logic(self):
        obj = self.num
        if 7 < (obj) < 40:
            a = 1
            b = (obj) - 8
            while True:
                if b > 7:
                    a += 1
                    b -= 8
                else:
                    return f'{a}d{b}h'
                    
        if 39 < (obj) < 160:
            a = 1
            b = 0
            c = (obj) - 40
            while True:
                if c > 7:
                    b += 1
                    c -= 8
                    if b > 4:
                        a += 1
                        b -= 5
                else:
                    return f'{a}w{b}d{c}h'
                
        if (obj) >= 160:
            a = 1
            b = 0
            c = 0
            d = (obj) - 160
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
        else:
            return str(obj) + 'h'


class ErrorApi(Exception):
    pass


class AuthenticationError(Exception):
    pass


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
        self.estimation = self.pars_estimation(estimation)
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
        
    def pars_estimation(self, estimation):
        obj = Estimation(estimation[:-1], estimation[-1:])
        return obj

    def get_board_id(self):
        try:
            with psycopg2.connect(** info_bd) as conn:
                with conn.cursor() as cursor:
                    request = "SELECT board_id FROM Boards where title ='{}'".format(self.board)
                    cursor.execute(request)
                    records = cursor.fetchall()
                    return records[0][0]
        except IndexError:
            raise ErrorApi
    
    def save_in_bd(self):
        if is_card(self.title, self.board):
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
        else: 
            raise ErrorApi

# a = Card
# data = {'title': 'Paint', 'board': 'Доска дизайнера', 'status': 'ToDo', 'description': 'Необходимо за весь карантин не поехать кукухой ', 'assignee': 'Mark', 'estimation': '1m', 'user_name': 'Bob', 'times': 1586702775.722399}

# a.create_from_dict(data)

# print(a)