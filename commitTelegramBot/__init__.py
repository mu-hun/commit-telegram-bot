import datetime
import random
from functools import reduce
from typing import Dict

import requests

warning_scripts = [
    '커밋좀;',
    '저기여, 커밋인데여. 오늘 커밋 안하세여?',
    '**커밋은 하고 자야지?**',
    '커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!~~빼애ㅐㅣ애애애액!!!!!!!!!~~',
    '커밋해야 한다(~~수화기를 들며~~)',
    '커밋 컴 윗 미 컴윗',
    '*Make Commit log Great Again*',
    '**1 Day 1 Commit** (찡긋)'
]

stickers = {
    'flushed': 'CAACAgIAAxkBAAMLYGrMzPUGdq4FTRqjgHz50d7yO7gAAiYLAAIvD_AGAx6skcPBsyAeBA',
    'thumbs_up': 'CAACAgIAAxkBAAMMYGrM00m6t8fGx5BfsoJxk-5Sea8AAlALAAIvD_AGpFqpz_st7RgeBA'
}


def get_warning_script(): return random.choice(warning_scripts)


class CommitTelegramBot:

    __slots__ = ['github_token', 'username', 'endpoint', 'chat_id']

    def __init__(self, github_token: str, username: str, bot_token: str, chat_id: str):
        self.github_token = github_token
        self.username = username
        self.endpoint = f'https://api.telegram.org/bot{bot_token}'
        self.chat_id = chat_id

    def fetch(self) -> Dict[str, int]:
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

        fetched = requests.post('https://api.github.com/graphql',
                                json={'query': query}, headers=header).json()

        return fetched['data']['user']['contributionsCollection']

    def send_sticker(self, file_id: str):
        requests.get(self.endpoint + '/sendSticker',
                     data={'chat_id': self.chat_id, 'sticker': file_id})

    def send_message(self, message: str):
        requests.post(self.endpoint + '/sendMessage',
                      data={'chat_id': self.chat_id, 'text': message, 'parse_mode': 'Markdown'})

    def handler(self):
        contributions = self.fetch()
        count = reduce(lambda count, value: count +
                       value, contributions.values(), 0)
        if count == 0:
            self.send_sticker(stickers['flushed'])
            self.send_message(get_warning_script())
        else:
            self.send_sticker(stickers['thumbs_up'])
            self.send_message('\n'.join(
                (
                    f'현재까지 `{count}` 개의 기여를 해냈습니다 👍',
                    f'• Commit: `{contributions["totalCommitContributions"]}`',
                    f'• Issue: `{contributions["totalIssueContributions"]}`',
                    f'• PR: `{contributions["totalPullRequestContributions"]}`',
                )))
