# commit-telegram-bot

[![Build Status](https://travis-ci.org/BetaF1sh/commit-telegram-bot.svg?branch=master)](https://travis-ci.org/BetaF1sh/commit-telegram-bot) 
[![PyPI version](https://badge.fury.io/py/commit-telegram-bot.svg)](https://badge.fury.io/py/commit-telegram-bot)

:alarm_clock: Remind your commit and coding every day with chat bot!

## Screenshot

<img src='screenshot.png' width='300em'>

## install

```bash
pip install commit-telegram-bot
```

## How to run

```python
>>> from commit-telegram-bot import commitTelegramBot
>>> bot = CommitTelegramBot('github_token', 'github_usrname', 'telegram_token', 'telegram_id')
>>> print(bot.count_total()) # print today's commit count
>>> bot.handler() # run bot
```

## License

_commit-telegram-bot_ is primarily distributed under the terms of the MIT License. see [LICENSE](./LICENSE) for details.
