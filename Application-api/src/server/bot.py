import requests
import json
from logic.core_logic import ClientWrapper


def main_bot(request):
    print(request.json)
    bot = TeleWrapper(request)
    # if bot.is_start():
    bot.send_message()
    # print(request.headers)


class TeleWrapper:
    def __init__(self, request):
        self.request = request

    def is_start(self):
        messege = self.request.json['message']['text']
        chat_id = self.request.json['message']['chat']['id']
        first_name = self.request.json['message']['chat']['first_name']

        if messege.lower() == 'start':
            print('Запуск бота')
            return True
        else:
            send_message = f'{first_name}, для начала работы введите "start", для помощи "help"'
            self.send_message(chat_id, send_message)

    # def send_message(self, chat_id, messege):
    #     method = "sendMessage"
    #     token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
    #     url = f"https://api.telegram.org/bot{token}/{method}"
    #     data = {"chat_id": chat_id, "text": messege}
    #     requests.post(url, data=data)
    #### кнопка со ссылкой
    # def send_message(self):
    #     chat_id = self.request.json['message']['chat']['id']
    #     method = "sendMessage"
    #     token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
    #     url = f"https://api.telegram.org/bot{token}/{method}"
    #     message_id = self.request.json["message"]["message_id"]

    #     reply = json.dumps({"inline_keyboard":[[{"text":"текст1","url":"http://ya.ru"}]]})
    #     params = {"chat_id": chat_id, "text": "!!!", "reply_markup":reply}
    #     requests.post(url, params)
    #### Кнопка которая пишет текст
    def send_message(self):
        chat_id = self.request.json['message']['chat']['id']
        method = "sendMessage"
        token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
        url = f"https://api.telegram.org/bot{token}/{method}"
        message_id = self.request.json["message"]["message_id"]

        reply = json.dumps({"keyboard":[[{"text":"текст1"}]]})
        params = {"chat_id": chat_id, "text": "!!!", "reply_markup": reply}
        requests.post(url, params)

        # requests.post(url, data=data)
# {'inline_keyboard':[[url_button, question_button],[switch_button]]}
    # def command(self):
    #     pass



# { "chat_id":" <id>","text": "Жмякай", "reply_markup": { "keyboard": [ [ {"text": "Кнопка 1"}, {"text": "Кнопка 2"} ], [ {"text": "Кнопка 3"}, {"text": "Кнопка 4"} ] ] } } 
# {'update_id': 457748742, 
# 'message': {'message_id': 72, 
#                 'from': {'id': 831026568, 
#                             'is_bot': False, 
#                             'first_name': 'Виктор', 
#                             'last_name': 'Овсиенко', 
#                             'username': 'ovsienko023', 
#                             'language_code': 'ru'}, 
#                 'chat': {'id': 831026568, 
#                         'first_name': 'Виктор',
#                         'last_name': 'Овсиенко', 
#                         'username': 'ovsienko023', 
#                         'type': 'private'}, 
#                         'date': 1587888836, 
#                         'text': 'q'}}
# ###