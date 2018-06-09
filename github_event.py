# coding : utf-8

import datetime
import json
from github import Github

with open('config.json') as config_file:
    config = json.load(config_file)

class GetEvent():
    def __init__(self):
        self.username = config['username']
        gh_token = config['gh_token']

        self.client = Github(gh_token)

    def handle(self):
        today_commit_events = get_today_commit_events(self.client.get_user(self.username))

        if len(today_commit_events) == 0:
            return False
        return True

def get_today_commit_events(user):
    today = datetime.datetime.today()
    today_date = datetime.datetime(today.year, today.month, today.day)

    commit_events = []

    for event in user.get_events():
        if event.created_at > today_date:
            if event.type in ['PushEvent', 'PullRequestEvent', 'IssueEvent']:
                commit_events.append(event)
        else:
            break

    return commit_events
