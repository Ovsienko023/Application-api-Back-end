import requests
from logic.core_logic import ClientWrapper


def main_bot(request):
    print(request.json)
    bot = TeleWrapper(request)
    bot.command()
    # print(request.headers)


class TeleWrapper:
    def __init__(self, request):
        self.request = request

    def command(self):
        messege = self.request.json['message']['text']
        chat_id = self.request.json['message']['chat']['id']
        first_name = self.request.json['message']['chat']['first_name']

        if messege.lower() == 'start':
            print('Запуск бота')
        else:
            send_message = f'{first_name}, для начала работы введите "start", для помощи "help"'
            self.send_message(chat_id, send_message)

    def send_message(self, chat_id, messege):
        method = "sendMessage"
        token = r"1026862035:AAG-mBQD7TgE_yaiE3uC38-W-Q5KRQ6uy1I"
        url = f"https://api.telegram.org/bot{token}/{method}"
        data = {"chat_id": chat_id, "text": messege}
        requests.post(url, data=data)

{'update_id': 457748742, 
'message': {'message_id': 72, 
                'from': {'id': 831026568, 
                            'is_bot': False, 
                            'first_name': 'Виктор', 
                            'last_name': 'Овсиенко', 
                            'username': 'ovsienko023', 
                            'language_code': 'ru'}, 
                'chat': {'id': 831026568, 
                        'first_name': 'Виктор',
                        'last_name': 'Овсиенко', 
                        'username': 'ovsienko023', 
                        'type': 'private'}, 
                        'date': 1587888836, 
                        'text': 'q'}}
###