import requests
from time import sleep

url="Https://api.telegram.org/bot1471709864:AAHMOhktDR6JwQ-rz5JlVa30pvmILBSdcHc/"
class BotHandler:

def __init__(self, token):
    self.token = '1471709864:AAHMOhktDR6JwQ-rz5JlVa30pvmILBSdcHc'
    self.api_url = "Https://api.telegram.org/bot{}/".format(token)

def get_updates(self, offset=None, timeout=30):
    method = 'getUpdates'
    params = {timeout} #Закончил тут -> https://tproger.ru/translations/telegram-bot-create-and-deploy/

def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def send_mess(chat, text):
    params = {'chat_id' : chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def main():
    update_id = last_update(get_updates_json(url))['update_id']
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), 'Не пиши сюда, мешок с мясом')
           update_id += 1
        sleep(1)

if __name__ == '__main__':
    main()