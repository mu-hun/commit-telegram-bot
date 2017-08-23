# coding : utf-8

import datetime
import json
from github import Github

with open('config.json') as config_file:
    CONFIG = json.load(config_file)

class GetEvent():
    def __init__(self):
        self.username = CONFIG['username']
        self.password = CONFIG['password']

    def handle(self):
        client = Github(self.username, self.password)
        today_commit_events = get_today_commit_events(client.get_user(self.username))

        if len(today_commit_events) == 0:
            return False
        else:
            return True

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
