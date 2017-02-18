# coding: utf-8

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import Job
from telegram import ParseMode

import datetime
import random

from commit_event import config
from commit_events import GetEvent

import logging
formats = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.DEBUG, format=formats)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

updater = Updater(config['bot_token'])
dispatcher = updater.dispatcher


def start(bot, update):
    msg = "안녕 {git_user}! 저는 커미이이잇 봇이에요.(찡긋) \n 커밋! 커밋을 보자!"
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         git_user=update.message.from_user.first_name,
                         bot_name=bot.name))


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="유효하지 않는 커맨드 입니다.")

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler([Filters.command], unknown))


message_list = [
    '커밋좀;',
    '저기여, 커밋인데여. 오늘 커밋 안하세여?',
    '<b>커밋은 하고 자야지?</b>',
    '커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<del>빼애ㅐㅣ애애애액!!!!!!!!!</del>',
    '커밋해야 한다(<del>수화기를 들며</del>)',
    '커밋 컴 윗 미 컴윗',
    '<i>Make Commit log Great Again</i>',
    '<b>1 Day 1 Commit</b> (찡긋)'
]
random_message = random.choice(message_list)

sticker_list = [
    'images/reva.webp',
    'images/cat.webp'
]
random_sticker = random.choice(sticker_list)

def plzcommit(bot, update):
    commitevent = GetEvent()
    user_status = commitevent.handle()
    if user_status == False:
        if random.randint(0, 1) == 0:
            bot.sendSticker(chat_id=config['tele_id'], sticker=open(random_sticker, 'rb'))
        else:
            bot.sendMessage(chat_id=config['tele_id'], text=random_message, parse_mode=ParseMode.HTML)
    else:
        print("commit status of user is Good :D")

# 3600 = One hour execute
job_minute = Job(plzcommit, 3600.0)
updater.job_queue.put(job_minute, next_t=0.0)

# Start the program
if __name__ == __main__:
    updater.start_polling()
    updater.idle()
