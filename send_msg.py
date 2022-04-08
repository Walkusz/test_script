"""
Naval Fate.

Usage: send_msg TEXT
"""
import os
import requests
from docopt import docopt

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT_CHAT_ID = os.environ.get('BOT_CHAT_ID')
BASE_STRING = 'https://api.telegram.org/bot' + BOT_TOKEN


def telegram_bot_sendtext(bot_message):
    send_text = BASE_STRING + '/sendMessage?chat_id=' + BOT_CHAT_ID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Test script v1')
    telegram_bot_sendtext(arguments['TEXT'])
