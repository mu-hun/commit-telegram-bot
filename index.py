# coding: utf-8

import random
import json
from requests import get

from github_event import GetEvent

with open('config.json') as config_file:
    config = json.load(config_file)

script = [
    '커밋! 커밋을 보자!',
    '커밋좀;',
    '<b>커밋은 하고 자야지?</b>',
    '저기여, 커밋인데여. 오늘 커밋 안하세여?',
    '커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<b>빼애ㅐㅣ애애애액!!!!!!!!!</b>',
    '커밋해야 한다(<b>수화기를 들며</b>)',
    '커밋 컴 윗 미 컴윗',
    '<i>Make Commit log Great Again</i>',
    '<b>1 Day 1 Commit</b> (찡긋)'
]
message = random.choice(script)

stickers = [
    'CAADBAADHgAD2Z41UFC5XtkuKo6FAg',
    'CAADBAADHQAD70EtUMSATFLKs-DHAg'
]
sticker = random.choice(stickers)

api = 'https://api.telegram.org/bot' + config['bot_token']
chat_id = config['tele_id']

def send_commit_status():
    commitevent = GetEvent()
    user_status = commitevent.handle()
    if user_status == 0:
        get(api + '/sendSticker', data={'chat_id':chat_id, 'sticker':sticker})
        get(api + '/sendMessage', data={'chat_id':chat_id, 'text':message, 'parse_mode':'HTML'})

# Start the program
if __name__ == "__main__":
    send_commit_status()
