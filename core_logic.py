import time


class User:
    def __init__(self, user_name, user_secret):
        self.user_name = user_name
        self.__user_secret = user_secret


class Board:
    required = ['user_name', 'title', 'columns']

    def __init__(self, user_name, title, columns):
        self.time = time.time()
        self.user_name = user_name
        self.title = title
        self.columns = ','.join(columns)


    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)


    def save_in_bd(self):
        print("отправленно")
# data = {'title': 'Доска разработчика', 'columns': ['ToDo', 'InProgress', 'Done'], 'user_name': 'Bob'}
# a = Board.create_from_dict(data)
# print(a)

class Card:
    required = ['user_name', 'title', 'board', 'status', 'description', 'assignee', 'estimation']

    def __init__(self, title, board, status, description, assignee, estimation):
        self.title = title
        self.board = board
        self.status = status
        self.description = description
        self.assignee = assignee
        self.estimation = estimation


    @classmethod
    def create_from_dict(cls, data):
        parameters = [data[parameter] for parameter in cls.required]
        return cls(*parameters)



class Estimation(int):
    """Descriptor"""




# user1 = User('Bob', '38rhh2824r2b27')
# board = Board('Bob', 'Доска разработчика', ["ToDo", "InProgress", "Done"])
# card = Card('Развернуть PostgreSQL', 'Доска разработчика', 'ToDo', 'Необходимо развернуть базу данных PostgreSQL', 'Jeck', '3h')

# print(card.status)
# print(board.columns)
