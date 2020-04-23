import psycopg2
import os

class WrapperDB:
    def __init__(self, obj):
        self.obj = obj
        self.info_db = info_db
        self.conn = psycopg2.connect(**info_db)
        self.cursor = self.conn.cursor()

    def config_app(self):
        path = os.getcwd() + "/config.txt"
        with open(path) as config:
            json_str = config.read()
            #print(config.read())
            return json.loads(json_str)

    info_bd = config_app()['Data_Base']

    
    def seve_board_in_db(self):
        if self.is_board(self.title):
            request = f"""INSERT INTO Boards (user_name, times, title, columns, board_id)
                        VALUES ('{self.user_name}', '{self.times}',
                        '{self.title}', '{self.columns}', {self.board_id})"""
            self.cursor.execute(request)
            return cursor.statusmessage
        else:
            raise ErrorApi

    def save_card_in_bd(self):
        if self.is_card(self.title, self.board):
            request = f"""INSERT INTO Cards (user_name, times, title, board, status,
                                                description, assignee, estimation, board_id, 
                                                last_update_at, last_update_by)
                        VALUES ('{self.user_name}', '{self.times}',
                        '{self.title}', '{self.board}', '{self.status}',
                        '{self.description}', '{self.assignee}', '{self.estimation}',
                        {self.board_id}, '{self.last_update_at}', '{self.last_update_by}')"""
            self.cursor.execute(request)
            return self.cursor.statusmessage
        else: 
            raise ErrorApi

    def is_board(self,board_name):
        with psycopg2.connect(**info_bd) as conn:
            with conn.cursor() as cursor:
                request = f"SELECT title FROM Boards where title = '{board_name}'"
                cursor.execute(request)
                status = cursor.statusmessage.split(' ')[1]
                if status == '1':
                    return False
                if status == '0': 
                    return True

    def is_card(self, card_name, board_name):
        """ func is_card reverse """
        request = f"SELECT title FROM Cards where title = '{card_name}' AND board = '{board_name}'"
        self.cursor.execute(request)
        status = cursor.statusmessage.split(' ')[1]
        if status == '0':
            return True
        else: 
            return False








    def close(self):
        self.conn.close()
        self.cursor.close()