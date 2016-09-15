# coding: utf-8

# from configparser import ConfigParser

import datetime
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import Job
from telegram import ParseMode

from github import Github


import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# TODO: .ini parser code of ConfigPaser bug Fix
# config = ConfigParser()
# config.read('config.ini')
#
#
# def get_telegram_info():
#     token = config['telegram']['token']
#     tele_id = config['telegram']['tele_id']
#
#     return token, tele_id
#
# token tele_id = get_telegram_info()
#
# def get_github_account_info():
#     user_name = config['github']['username']
#     pass_word = config['github']['password']
#
#     return user_name, pass_word


updater = Updater('token')
dispatcher = updater.dispatcher


def start(bot, update):
    # Home message
    msg = "안녕 {user_name}! 저는 커미이이잇 봇이에요.(찡긋) \n"
    msg += "커밋! 커밋을 보자!"

    # Send the message
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name,
                         bot_name=bot.name))


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="유효하지 않는 커맨드 입니다.")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler([Filters.command], unknown))

message_list = [
    u'커밋좀;',
    u'저기여, 커밋인데여. 오늘 커밋 안하세여?',
    u'<b>커밋은 하고 자야지?</b>',
    u'커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<del>빼애ㅐㅣ애애애액!!!!!!!!!</del>',
    u'커밋해야 한다(<del>수화기를 들며</del>)',
    u'커밋 컴 윗 미 컴윗',
    u'<i>Make Commit log Great Again</i>',
    u'<b>1 Day 1 Commit</b> (찡긋)'
]

sticker_list = [
    u'http://gdurl.com/zy7Z',
    u'http://gdurl.com/eRGt'
]


def get_today_commit_events(user):
    today = datetime.datetime.today()
    today_date = datetime.datetime(today.year, today.month, today.day)
    today_date_ko = today_date - datetime.timedelta(hours=9)

    commit_events = []

    for event in user.get_events():
        if event.created_at > today_date_ko:
            if event.type in ['PushEvent', 'PullRequestEvent', 'IssueEvent']:
                commit_events.append(event)
        else:
            break

    return commit_events


def handle(bot, job):
    username, password = 'your_username', 'your_pw'# username, password = get_github_account_info()

    client = Github(username, password)

    today_commit_events = get_today_commit_events(client.get_user(username))

    if len(today_commit_events) == 0:
        # NOTE : 'tele_id' is your telegram id please check your id to https://telegram.me/userinfobot
        if random.randint(0, 1) == 0:
            bot.sendSticker(chat_id='tele_id', sticker=random.choice(sticker_list))
        else:
            bot.sendMessage(chat_id='tele_id', text=random.choice(message_list), parse_mode=ParseMode.HTML)


job_minute = Job(handle, 3600.0) # 3600s(1h) execute

j = updater.job_queue
j.put(job_minute, next_t=0.0)

# start the program
updater.start_polling()
updater.idle()
