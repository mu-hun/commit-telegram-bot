# commit-telegram-bot

:alarm_clock: Remind your commit and coding every day with chat bot!

## How to run this chat bot

  1. `pip install -r requirements.txt`
  2. `./setup.sh`
  3. `python index.py`

## You can also use cron job

```bash
$ crontab -e
#/usr/bin/crontab
0 9-23/3 * * * /Users/muhun/.local/share/virtualenvs/commit-telegram-bot-0yJ9B3aR/bin/python3 /Users/muhun/github/betaFish/commit-telegram-bot/index.py
```

`~/.local/share/virtualenvs/commit-telegram-bot-0yJ9B3aR` and `~/github/betaFish` is my own directory environment

Repeat every 3 hours from 9:00 to 23:00.

## Screenshot

<img src='screenshot.png' width='300em'>

## Default bot chat script

```html
'커밋좀;',
'저기여, 커밋인데여. 오늘 커밋 안하세여?',
'<b>커밋은 하고 자야지?</b>',
'커밋하세에ㅔㅔㅔㅔㅁㅁㅁ!!!!<del>빼애ㅐㅣ애애애액!!!!!!!!!</del>',
'커밋해야 한다(<del>수화기를 들며</del>)',
'커밋 컴 윗 미 컴윗',
'<i>Make Commit log Great Again</i>',
'<b>1 Day 1 Commit</b> (찡긋)'
```

## License

orignal project : [geekhub-lab/commit-alarm](https://github.com/geekhub-lab/commit-alarm)

_commit-telegram-bot_ is primarily distributed under the terms of the MIT License. see [LICENSE](./LICENSE) for details.
