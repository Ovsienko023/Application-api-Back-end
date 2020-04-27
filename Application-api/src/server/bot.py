import requests
import json
from logic.core_logic import ClientWrapper


def main_bot(request):
    print(request.json)
    bot = TeleWrapper(request)
    # if bot.is_start():
    
    # bot.send_message('Hi')
    bot.inline_keyboard()
    # print(request.headers)


class TeleWrapper:
    def __init__(self, request):
        self.request = request
        self.token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
        self.method = "sendMessage"
        self.url = f"https://api.telegram.org/bot{self.token}/{self.method}"

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

    def send_message(self, messege):
        chat_id = self.request.json['message']['chat']['id']
        data = {"chat_id": chat_id, "text": messege}
        requests.post(self.url, data=data)
    
    #### кнопка со ссылкой
    def inline_keyboard(self):
        """ Link button """

        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json["message"]["message_id"]

        reply = json.dumps({"inline_keyboard":[[{"text":"Ниги","url":"https://memepedia.ru/negry-s-grobom/"}]]})
        params = {"chat_id": chat_id, "text": "!!!", "reply_markup":reply}
        requests.post(self.url, params)
    
    #### Кнопка которая пишет текст
    def keyboard(self):
        """ Button """
        
        chat_id = self.request.json['message']['chat']['id']
        message_id = self.request.json["message"]["message_id"]

        reply = json.dumps({"keyboard":[[{"text":"текст1"}]]})
        params = {"chat_id": chat_id, "text": "!!!", "reply_markup": reply}
        requests.post(self.url, params)




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