# coding: utf-8

from configparser import ConfigParser

import datetime
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from github import Github


def get_telegram_token_url():
    parser = ConfigParser()
    parser.read('config/telegram.ini')

    return parser.get('telegram', 'telegram_token')


updater = Updater(token=get_telegram_token_url())
dispatcher = updater.dispatcher


def start(bot, update):
    # Home message
    msg = "안녕 {user_name}! 저는 {bot_name} 챗봇이에요. \n"
    msg += "커밋! 커밋을 보자!"

    # Send the message
    bot.send_message(chat_id=update.message.chat_id,
                     text=msg.format(
                         user_name=update.message.from_user.first_name,
                         bot_name=bot.name))


def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="유효하지 않는 커맨드 입니다.")


# telegram bot api Handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler([Filters.command], unknown))

message_list = [
    u'커밋좀;',
    u'저기여, 커밋인데여. 오늘 커밋 안하세여?',
    u'커밋은 하고 자야지?',
    u'커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!빼애ㅐㅣ애애애액!!!!!!!!!',
    u'커밋해야 한다(수화기를 들며)',
    u'커밋 컴 윗 미 컴윗',
    u'Make Commit log Great Again',
    u'1 Day 1 Commit (찡긋)'
]


def get_github_account_info():
    parser = ConfigParser()
    parser.read('config/github.ini')

    username = parser.get('github', 'username')
    password = parser.get('github', 'password')

    return username, password


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


def handle(bot):
    username, password = get_github_account_info()

    client = Github(username, password)

    today_commit_events = get_today_commit_events(client.get_user(username))

    if len(today_commit_events) == 0:
        bot.sendMessage(chat_id='', text=random.choice(message_list))


# start the program
updater.start_polling()
