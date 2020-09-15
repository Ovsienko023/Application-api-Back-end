# Scrum Board Api v3.0

Может использоваться при разработке по методологии Scrum. Для управления досками и задачами необходимо использовать POST и GET запросы на сервер. Все методы api имеют префикс: `http://127.0.0.1:5000/api/v3/ваш_запрос`. 
Для всех методов api передаются заголовки POST запроса: User_Name - имя пользователя, User_Secret - токен пользователя.

* На все удачные запросы возвращается json c данным или {"ok":True}. 

* В случае неудачи: {"Error": "Value"} 
* В случае ошибки идентификации: {"status": False, "info": "Authentication Error"}

## Для начала работы с api необходимо:

1. Установить все зависимости 
`$ pip install -r requirements.txt`
2. Запустить сервер базы данных - PostgreSQL, убедиться что БД пуста (при первом включении)
3. В файле config.txt записать параметры забуска БД и сервера:

		    {"server":{"host": "Хост сервера", 
                       "port": "Порт Сервера"}, 
             "Data_Base":{"dbname": "Имя БД", 
                   	 	  "user": "Пользователь", 
                     	  "password": "Пароль", 
                    	  "host":"Хост сервера"}
4. Выполнить в терминале команды: 

		$ make build
		ok
		$ make test
		ok
		$ make run
	После этого будет запущен сервер и api готов к работе.
	
## Начало работы с api
Примеры работы:

Пользователь для теста api:
login = Bob
passsword = 123

Все примеры написанны на python3 c использованием модуля requests

#### Создание доски:

            def create_board():
                url = r'http://127.0.0.1:5000/api/v3/board/create'
                data = {
                    "title": "Доска Дворника 1",
                    "columns": [
                        "Пойти",
                        "Убрать",
                        "Уйти"
                ] }
                response = requests.post(url, json=data, auth=(login, passsword))
                print(response.content)

#### Удаление доски

            def delete_board():
                url = r'http://127.0.0.1:5000/api/v3/board/delete'
                data = {
                    "title": "Доска Дворника 1",
                }

                response = requests.delete(url, params=data, auth=(login, passsword))
                print(response.json())

#### Создание Карточки

            def create_card():
                url = r'http://127.0.0.1:5000/api/v3/card/create'
                data = {
                    "title": "Painter_",
                    "board": "Доска Дворника 1",
                    "status": "Пойти",
                    "description": "Необходимо за весь карантин не поехать кукухой ",
                    "assignee": "Mark",
                    "estimation": "1m"
                }
                response = requests.post(url, json=data, auth=(login, passsword))
                print(response.json())

#### Обновление Карточки

            def update_card():
                url = r'http://127.0.0.1:5000/api/v3/card/update'
                data = {
                    "title": "Painter_",
                    "board": "Доска Дворника 1",
                    "assignee": "Karlos"
                }

                response = requests.put(url, json=data, auth=(login, passsword))
                print(response.content)

#### Удаление Карточки

            def delete_card():
                url = r'http://127.0.0.1:5000/api/v3/card/delete'
                data = {
                    "title": "Painter_",
                    "board": "Доска Дворника 1"
                }

                response = requests.delete(url, params=data, auth=(login, passsword))
                print(response.content)

#### Отчет по колонке
Этот отчет позволяет получить информацию о задачах, которые находятся в определенной колонке. Например, чтобы посмотреть сколько задач запланировано на определенного пользователя, сколько сейчас в работе, а сколько уже завершено.

            def report():
                url = r'http://127.0.0.1:5000/api/v3/report/cards_by_column'
                data = {
                    "board": "Доска Дворника 1",
                    "column": "Пойти",
                    "assignee": "Karlos"
            		    }
                response = requests.get(url, params=data, auth=(login, passsword))
                print(response.json())

#### Список пользователей
            def board_list():
                url = r'http://127.0.0.1:5000/api/v3/board/list'
                response = requests.get(url, auth=(login, passsword))
                print(response.json())
