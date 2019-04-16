# encoding: utf-8
import json
from pprint import pprint
from time import sleep
import urllib
import urllib2
from config import TOKEN
import random
# import logging


class TelegramBot(object):
    def __init__(self):
        self.base_url = "https://api.telegram.org/bot" + TOKEN + "/"
        self.offset = 0

    def get_me(self):
        print("test")
        response = json.load(urllib2.urlopen(self.base_url + "getMe"))
        return response['ok']

    def get_updates(self):
        data = {
            "offset": self.offset
        }
        response = json.load(urllib2.urlopen(self.base_url + "getUpdates", urllib.urlencode(data)))
        if len(response['result']) > 0:
            self.offset = response['result'][-1]['update_id'] + 1
        return response['result']

    def send_message(self, msg, chat_id, reply_id=None):
        data = {
            "chat_id": chat_id,
            "text": msg,
        }
        if reply_id is not None:
            data["reply_to_message_id"] = reply_id
        response = json.load(urllib2.urlopen(self.base_url + "sendMessage", urllib.urlencode(data)))
        #pprint(response)


def polling():
    bot = TelegramBot()
    print bot.get_me()

    while True:
        for in_message in bot.get_updates():
            #pprint(in_message)
            try:
                message = in_message['message']
                process_super_hot(message, bot)
            except Exception as err:
                print("Error in processing message {}".format(err))
            # bot.send_message(message['text'], message['chat']['id'], message['message_id'])
        sleep(1)

def process_super_hot(message, bot_instance):
    print(message)
    if message["text"] == "/HOT" or message["text"] == "/hot":
        bot_instance.send_message("/SUPER", message['chat']['id'], message['message_id'])
    if message["text"] == "/SUPER" or message["text"] == "/super":
        bot_instance.send_message("/HOT", message['chat']['id'], message['message_id'])
    if message["text"] == "/SUPERHOT" or message["text"] == "/superhot":
        bot_instance.send_message("SUPER HOT " * random.randint(0,100), message['chat']['id'], message['message_id'])



if __name__ == "__main__":
    polling()
