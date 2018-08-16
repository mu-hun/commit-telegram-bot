# coding: utf-8
from datetime import date
import json
import random

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

message = random.choice(script)

stickers = [
    'CAADBAADHgAD2Z41UFC5XtkuKo6FAg',
    'CAADBAADHQAD70EtUMSATFLKs-DHAg'
]
sticker = random.choice(stickers)

date = date.today()
year, month, day = str(date.year), date.strftime('%m'), date.strftime('%d')

class CommitTelegramBot:
	def __init__(self, github_token, github_user, telegram_token, telegram_id):
		self.header = {"Authorization": "Bearer " + github_token}
		self.query_access = {"query": "query{user(login: " + github_user + ") { repositories(last: 100) { totalCount nodes { name defaultBranchRef { target { ...on Commit {history(since: \"" + year + "-" + month + "-" + day + "T09:00:00+00:00\") { totalCount}}}}}}}}"}
		self.api = 'https://api.telegram.org/bot' + telegram_token
		self.chat_id = telegram_id
		
	def fetch_data(self):
		return requests.post("https://api.github.com/graphql", data=json.dumps(self.query_access), headers=self.header).json()
	
	def count_total(self):
		data, count = self.fetch_data(), 0
		for atom in data['data']['user']['repositories']['nodes']:
			if atom['defaultBranchRef'] is not None:
				count = count + atom['defaultBranchRef']['target']['history']['totalCount']
		return count

	def handler(self):
		if self.count_total() is 0:
			requests.get(self.api + '/sendSticker', data={'chat_id':self.chat_id, 'sticker':sticker})
			requests.get(self.api + '/sendMessage', data={'chat_id':self.chat_id, 'text':message, 'parse_mode':'HTML'})
		else:
			requests.get(self.api + '/sendMessage', data={'chat_id':self.chat_id, 'text': '현재까지 %d 개의 커밋을 해냈습니다!' % self.count_total()})
