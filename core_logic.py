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


class Estimation(int):
    """Descriptor"""




# user1 = User('Bob', '38rhh2824r2b27')
# board = Board('Bob', 'Доска разработчика', ["ToDo", "InProgress", "Done"])
# card = Card('Развернуть PostgreSQL', 'Доска разработчика', 'ToDo', 'Необходимо развернуть базу данных PostgreSQL', 'Jeck', '3h')

# print(card.status)
# print(board.columns)
