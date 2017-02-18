# coding: utf-8

import json
from github import Github

json = open('config/config.json').read()
config = json.loads(json)

class GetEvent():
    def __init__(self):
        self.username = config['username']
        self.password = config['password']

    def handle(self):
        client = Github(self.username, self.password)
        today_commit_events = get_today_commit_events(client.get_user(self.username))

        if len(today_commit_events) == 0:
            return False


def get_today_commit_events(self):
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
