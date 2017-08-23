# coding: utf-8

import random
import json

from github_event import GetEvent
import telepot

with open('config.json') as config_file:
    CONFIG = json.load(config_file)

BOT = telepot.Bot(CONFIG['bot_token'])
SCRIPT_LIST = [
    '커밋! 커밋을 보자!',
    '커밋좀;',
    '<b>커밋은 하고 자야지?</b>',
    '저기여, 커밋인데여. 오늘 커밋 안하세여?',
    '커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<del>빼애ㅐㅣ애애애액!!!!!!!!!</del>',
    '커밋해야 한다(<del>수화기를 들며</del>)',
    '커밋 컴 윗 미 컴윗',
    '<i>Make Commit log Great Again</i>',
    '<b>1 Day 1 Commit</b> (찡긋)'
]
RANDOM_MESSAGE = random.choice(SCRIPT_LIST)

STAKER_LIST = [
    'images/reva.webp',
    'images/cat.webp'
]
RANDOM_STICKER = random.choice(STAKER_LIST)

def send_commit_status():
    commitevent = GetEvent()
    user_status = commitevent.handle()
    if user_status == 0:
        # BOT.sendMessage(chat_id=CONFIG['tele_id'], sticker=open(RANDOME_STICKER, 'rb'))
        # TODO: add html parse_mode
        BOT.sendMessage(chat_id=CONFIG['tele_id'], text=RANDOM_MESSAGE, parse_mode=None)

# Start the program
if __name__ == "__main__":
    send_commit_status()
