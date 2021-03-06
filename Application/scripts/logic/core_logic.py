import psycopg2
import time
import json
import os
from logger.log import MyLogging
import logging

super_logger = MyLogging().setup_logger('core_logic',
                                        'Application/logger/logfile.log')#, logging.INFO)

class ErrorApi(Exception):
    pass


class AuthenticationError(Exception):
    pass


class ConnectError(Exception):
    pass


class Estimation:
    def __init__(self, num_all):
        self.num = num_all[:-1]
        self.cal = num_all[-1]
        if self.cal == 'd':
            self.num = int(self.num) * 8 
        if self.cal == 'w':
            self.num = int(self.num) * 40
        if self.cal == 'm':
            self.num = int(self.num) * 160 
        if self.cal == 'h':
            self.num = int(self.num)
        self.lst_obj = []

    
    def __add__(self, obj):
        sum_str = self.num + obj.num
        sum_str = str(sum_str) + 'h'
        return Estimation(sum_str)
   
        
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
        return str(self.num) + 'h'

    
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


class Board:
    required = ['user_name', 'title', 'columns', ]

    def __init__(self, user_name, title, columns):
        self.times = time.time()
        self.user_name = user_name
        self.title = title
        self.columns = self.valid_columns(columns)

    def valid_columns(self, columns):
        if isinstance(columns, list):
            columns = ','.join(columns)
            return columns
        else:
            raise ErrorApi

    @classmethod
    def create_from_dict(cls, data):
        print(data)
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)


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
        self.estimation = Estimation(estimation)
        self.last_update_at = time.time()
        self.last_update_by = user_name

    @classmethod
    def create_from_dict(cls, data):
        try:
            parameters = [data[parameter] for parameter in cls.required]
            return cls(*parameters)
        except TypeError:
            raise ErrorApi
        

class ConnectDB():
    """Creating a connection to the database."""
    def __init__(self):
        self.info_db = self.get_info_db()
        self.conn = psycopg2.connect(**self.info_db)
        self.cur = self.conn.cursor()

    def config_app(self):
        path = os.getcwd() + "/Application/config.json"
        with open(path) as config:
            json_str = config.read()
            return json.loads(json_str)

    def get_info_db(self):
        info_db = self.config_app()['Data_Base']
        return info_db

    def query(self, request):
        self.cur.execute(request)
        self.conn.commit()

    def toyal(self):
        return self.cur.fetchall()

    def status(self):
        return self.cur.statusmessage

    def close(self):
        self.cur.close()
        self.conn.close()


class SendObjDB:
    """Sending objects to the database."""
    def __init__(self, obj):
        self.obj = obj
        self.cursor = ConnectDB()

    def is_board(self, board_name):
        """ func is_board reverse """
        request = f"SELECT title FROM Boards where title = '{board_name}'"
        self.cursor.query(request)
        status = self.cursor.status().split(' ')[1]
        if status == '1':
            return False
        if status == '0': 
            return True

    
    def is_card(self, card_name, board_name):
        """ func is_card reverse """
        request = f"SELECT title FROM Cards where title = '{card_name}' AND board = '{board_name}'"
        self.cursor.query(request)
        status = self.cursor.status().split(' ')[1]
        if status == '0':
            return True
        else: 
            return False

    def save_board_in_db(self):
        if self.is_board(self.obj.title):
            request = f"""INSERT INTO Boards (user_name, times, title, columns)
                        VALUES ('{self.obj.user_name}', '{self.obj.times}',
                        '{self.obj.title}', '{self.obj.columns}')"""
            self.cursor.query(request)
            return self.cursor.status()
        else:
            raise ErrorApi

    def save_card_in_bd(self):
        if self.is_card(self.obj.title, self.obj.board):
            request = f"""INSERT INTO Cards (user_name, times, title, board, status,
                                                description, assignee, estimation, 
                                                last_update_at, last_update_by)
                        VALUES ('{self.obj.user_name}', '{self.obj.times}',
                        '{self.obj.title}', '{self.obj.board}', '{self.obj.status}',
                        '{self.obj.description}', '{self.obj.assignee}', '{self.obj.estimation}',
                        '{self.obj.last_update_at}', '{self.obj.last_update_by}')"""
            self.cursor.query(request)
            return self.cursor.status()
        else: 
            raise ErrorApi
    
    def __del__(self):
        self.cursor.close()


class DataInDB:
    """Writing data to the database."""
    cursor = ConnectDB()

    @classmethod
    def get_users(cls):
        users = {'users': []}

        cls.cursor.query('SELECT user_name, user_secret FROM Users')
        records = cls.cursor.toyal()
        for typles in records:
            user_name, user_secret = typles
            _ = dict()
            _['user_name'] = user_name
            _['user_secret'] = user_secret
            users['users'].append(_)
        return users

    @classmethod
    def get_boards(cls):
        boards = {'boards': []}

        cls.cursor.query('SELECT * FROM Boards')
        records = cls.cursor.toyal()
        for typles in records:
            user_name, times, title, columns = typles
            _ = dict()
            _['user_name'] = user_name
            _['times'] = times
            _['title'] = title
            _['columns'] = columns.split(',')
            boards['boards'].append(_)
        return boards
    
    @classmethod
    def get_cards(cls):
        cards = {'cards': []}
        
        cls.cursor.query('SELECT * FROM Cards')
        records = cls.cursor.toyal()
        for typles in records:
            user_name, times, title, board, status, description, assignee, estimation = typles
            _ = dict()
            _['user_name'] = user_name
            _['times'] = times
            _['title'] = title
            _['board'] = board
            _['status'] = status
            _['description'] = description
            _['assignee'] = assignee
            _['estimation'] = estimation
            cards['cards'].append(_)
        return cards

    # @classmethod
    # def delete(cls, data, tabl_name):
    #     title = data['title']
    #     if tabl_name == 'board':
    #         request = f"DELETE FROM Boards WHERE title = '{title}'"
    #         cls.cursor.query(request) 
    #         return cls.cursor.status()
    #     if tabl_name == 'card':
    #         board = data['board']
    #         return cls.delete_card(title, board)

    @classmethod
    def get_card(cls, name_card, name_board):
        try:
            request = f""" SELECT user_name, times, title,
                            board, status, description, assignee,
                            estimation, last_update_at, last_update_by
                            FROM Cards 
                            where title = '{name_card}'
                            AND board = '{name_board}'
                    """
            cls.cursor.query(request)
            records = cls.cursor.toyal()
            for typles in records:
                (user_name, times, title, board,
                status, description, assignee, estimation,
                last_update_at, last_update_by) = typles
                
                card = dict()
                card['user_name'] = user_name
                card['times'] = times
                card['title'] = title
                card['board'] = board
                card['status'] = status
                card['description'] = description
                card['assignee'] = assignee
                card['estimation'] = estimation
                card['last_update_at'] = last_update_at
                card['last_update_by'] = last_update_by
            cls.delete_card(title, board)
            return card
        except UnboundLocalError:
            return ''

    @classmethod
    def delete_card(cls, title, board):
        request = f"DELETE FROM Cards WHERE title = '{title}' and board = '{board}'"
        cls.cursor.query(request)
        return cls.cursor.status()

    @classmethod
    def delete_board(cls, title, user_name):
        request = f"DELETE FROM Boards WHERE title = '{title}' and user_name = '{user_name}'"
        cls.cursor.query(request)
        return cls.cursor.status()

    @classmethod
    def report(cls, data):
        status = data['column']
        name_board = data['board']
        user = data['assignee']
        request = f""" SELECT user_name, times, title,
                            board, status, description, assignee,
                            estimation, last_update_at, last_update_by
                            FROM Cards 
                            where assignee = '{user}'
                            AND status = '{status}'
                            AND board = '{name_board}'
                    """
        cls.cursor.query(request)
        return cls.cursor.toyal()

    @classmethod
    def is_authentication(cls, user_name, user_secret):
        request = f""" SELECT user_name, user_secret FROM Users 
                        WHERE user_name = '{user_name}'"""
        cls.cursor.query(request)
        return cls.cursor.toyal()

class DataInJson:
    """Methods for converting data from db to json."""
    @classmethod
    def pars_for_rep(cls, lst_card):
        """ Method for parser in json """
        try:
            json_card = dict()
            sum_estimation = list()
            lst = list()
            for card in lst_card:
                (user_name, times, title, board,
                status, description, assignee, estimation,
                last_update_at, last_update_by) = card

                sum_estimation.append(estimation)
                lst.append({
                            "title": title,
                            "board": board,
                            "status": status,
                            "description": description, 
                            "assignee": assignee,
                            "estimation": str(Estimation(estimation).pars()),
                            "created_at": time.ctime(float(times)),#### Сделать перевод
                            "created_by": user_name,
                            "last_updated_at": time.ctime(float(last_update_at)),#### Сделать перевод
                            "last_updated_by": last_update_by
                            })

            sum_e = Estimation('0h')
            for estam in sum_estimation:
                sum_e += Estimation(estam)
            json_card['board'] = board
            json_card['column'] = status
            json_card['assignee'] = assignee
            json_card['count'] = len(lst_card)
            json_card['estimation'] = str(sum_e.pars())
            json_card['cards'] = lst
            json_card = json.dumps(json_card)
            return json_card
        except UnboundLocalError:
            raise ErrorApi

    @classmethod
    def update_card(cls, data, user_name):
        try:
            name_card = data['title']
            name_board = data['board']
            card = DataInDB.get_card(name_card, name_board)
            obj_card = Card.create_from_dict(card)
            obj_card = cls.update_obj(data, obj_card, user_name)
            status = SendObjDB(obj_card).save_card_in_bd()            
            return status

        except ErrorApi:
            return ''

    @classmethod
    def update_obj(cls, data, obj, user_name):
        update_list = ['status', 'description', 'assignee', 'estimation']
        
        for key in ['title', 'board']:
            if data.get(key): data.pop(key)
        for key in data:
            if key == 'status':
                obj.status = data[key]
            if key == 'description':
                obj.description = data[key]
            if key == 'assignee':
                obj.assignee = data[key]
            if key == 'estimation':
                obj.estimation = data[key]
            if key not in update_list:
                raise ErrorApi
        obj.last_update_by = user_name
        return obj


class Destributor:
    def __init__(self, user_name, data=None):
        self.user_name = user_name
        self.data = data

    def user_list(self):
        try: 
            list_user = DataInDB.get_users()['users']
            count = len(list_user)
            status = {"count" :count, 
                            "users": [{'username':i['user_name']} for i in list_user] }
            return status
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, user_list")
            return {"status": False, "info": "ErrorApi"}
    
    def board_list(self):
        status = DataInDB.get_boards()
        return status

    def response_handler(self, answer):
        """Database Response Handler."""
        if answer == "Error" or answer == 'DELETE 0' or answer == '':
            return {"Error": "Value"}
        if answer == 'ok' or answer == 'INSERT 0 1' or answer == 'DELETE 1':
            return {"ok":True}
        if answer:
            return answer

    def board_creat(self):
        try:
            self.data['user_name'] = self.user_name
            self.data['times'] = time.time()
            obj_board = Board.create_from_dict(self.data)
            answer = SendObjDB(obj_board).save_board_in_db()
            answer = self.response_handler(answer)
            return answer
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, board_creat")
            return {"status": False, "Error": "Value"}

    def board_delete(self):
        try:
            answer = str(DataInDB.delete_board(self.data, self.user_name))
            answer = self.response_handler(answer)
            return answer
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, board_delete")
            return {"status": False, "Error": "Value"}

    def card_create(self):
        try:
            self.data['user_name'] = self.user_name
            self.data['times'] = time.time()
            obj_board = Card.create_from_dict(self.data)
            answer = SendObjDB(obj_board).save_card_in_bd()
            answer = self.response_handler(answer)
            return answer
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, card_create")
            return {"status": False, "Error": "Value"}
    
    def card_update(self):
        try:
            answer = DataInJson.update_card(self.data, self.user_name)
            answer = self.response_handler(answer)
            return answer
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, card_update")
            return {"status": False, "Error": "Value"}
    
    def card_delete(self):
        try:
            title = self.data['title']
            board = self.data['board']
            answer = str(DataInDB.delete_card(title, board))
            answer = self.response_handler(answer)
            return answer
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, card_delete")
            return {"status": False, "Error": "Value"}

    def report(self):
        try:
            lst_report = DataInDB.report(self.data)
            print(lst_report)
            return DataInJson.pars_for_rep(lst_report)
        except ErrorApi:
            super_logger.error(f"user: {self.user_name}, report")
            return {"status": False, "Error": "Value"}
