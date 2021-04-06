import datetime
import random
from functools import reduce
from typing import Dict

import requests

script = [
    '커밋좀;',
    '저기여, 커밋인데여. 오늘 커밋 안하세여?',
    '<b>커밋은 하고 자야지?</b>',
    '커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<del>빼애ㅐㅣ애애애액!!!!!!!!!</del>',
    '커밋해야 한다(<del>수화기를 들며</del>)',
    '커밋 컴 윗 미 컴윗',
    '<i>Make Commit log Great Again</i>',
    '<b>1 Day 1 Commit</b> (찡긋)'
]

stickers = {
    'flushed': 'CAACAgIAAxkBAAMLYGrMzPUGdq4FTRqjgHz50d7yO7gAAiYLAAIvD_AGAx6skcPBsyAeBA',
    'thumbs_up': 'CAACAgIAAxkBAAMMYGrM00m6t8fGx5BfsoJxk-5Sea8AAlALAAIvD_AGpFqpz_st7RgeBA'
}


def getScript(): return random.choice(script)


class CommitTelegramBot:

    __slots__ = ['github_token', 'username', 'endpoint', 'chat_id']

    def __init__(self, github_token: str, username: str, bot_token: str, chat_id: str):
        self.github_token = github_token
        self.username = username
        self.endpoint = f'https://api.telegram.org/bot{bot_token}'
        self.chat_id = chat_id

    def fetch(self):
        date = datetime.date.today()
        query = '''
        query {
          user(login: "%(username)s") {
            contributionsCollection(from: "%(date)sT00:00:00+00:00") {
              totalCommitContributions
              totalIssueContributions
              totalPullRequestContributions
            }
          }
        }
        ''' % {'username': self.username, 'date': date.isoformat()}

        header = {'Authorization': f'Bearer {self.github_token}'}

        return requests.post('https://api.github.com/graphql',
                             json={'query': query}, headers=header).json()

    def total_count(self):
        fetched = self.fetch()
        print(fetched)
        contributions_collection: Dict[str,
                                       int] = fetched['data']['user']['contributionsCollection']

        return reduce(lambda count, value: count + value, contributions_collection.values(), 0)

    def send_sticker(self, file_id: str):
        requests.get(self.endpoint + '/sendSticker',
                     data={'chat_id': self.chat_id, 'sticker': file_id})

    def handler(self):
        count = self.total_count()
        if count == 0:
            self.send_sticker(stickers['flushed'])
            requests.post(self.endpoint + '/sendMessage',
                          data={'chat_id': self.chat_id, 'text': getScript(), 'parse_mode': 'HTML'})
        else:
            self.send_sticker(stickers['thumbs_up'])
            requests.post(self.endpoint + '/sendMessage', data={
                'chat_id': self.chat_id, 'text': f'현재까지 {count} 개의 기여를 해냈습니다!'})
