import time
import psycopg2

# class User:
#     def __init__(self, user_name, user_secret):
#         self.user_name = user_name
#         self.__user_secret = user_secret


class Board:
    required = ['user_name', 'title', 'columns', ]

    def __init__(self, user_name, title, columns):
        self.times = time.time()
        self.user_name = user_name
        self.title = title
        self.columns = ','.join(columns)
        self.board_id = int(str(hash(self.times))[:5])


    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        print(parameters)
        return cls(*parameters)


    def save_in_bd(self):
        
        print("отправленно")


class Card:
    required = ['user_name', 'title', 'board', 'status', 'description', 'assignee', 'estimation']

    def __init__(self, user_name, title, board, status, description, assignee, estimation):
        self.times = time.time()
        self.user_name = user_name
        self.title = title
        self.board = board
        self.status = status
        self.description = description
        self.assignee = assignee
        self.estimation = estimation
        self.board_id = self.get_board_id()

    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)

    def get_board_id(self):
        with psycopg2.connect(dbname='my_data_base', user='ovsienko023', 
                            password='68471325', host='localhost') as conn:
            with conn.cursor() as cursor:
                request = "SELECT board_id FROM Boards where title ='{}'".format(self.board)
                cursor.execute(request)
                records = cursor.fetchall()
                return records[0][0]


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





