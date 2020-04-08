import time


class User:
    def __init__(self, user_name, user_secret):
        self.user_name = user_name
        self.__user_secret = user_secret


class Board:
    def __init__(self, user_name, title, columns):
        self.time = time.time()
        self.user_name = user_name
        self.title = title
        self.columns = columns


class Card:
    def __init__(self, title, board, status, description, assignee, estimation):
        self.title = title
        self.board = board
        self.status = status
        self.description = description
        self.assignee = assignee
        self.estimation = estimation





class Estimation(int):
    """Descriptor"""




user1 = User('Bob', '38rhh2824r2b27')
board = Board('Bob', 'Доска разработчика', ["ToDo", "InProgress", "Done"])
card = Card('Развернуть PostgreSQL', 'Доска разработчика', 'ToDo', 'Необходимо развернуть базу данных PostgreSQL', 'Jeck', '3h')

print(card.status)
print(board.columns)