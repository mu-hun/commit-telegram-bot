# commit-telegram-bot

![Test](https://github.com/x86chi/commit-telegram-bot/workflows/Test/badge.svg)

:alarm_clock: Remind your commit and coding every day with chat bot!

## Screenshot

<img src='screenshot.png' width='300em'>

I used [Mr. Deadline](https://t.me/addstickers/MrClockwise) stickers.

## Usage

Require minimum Python version is 3.6.

1. Clone this repository
2. Add below environment variables. You can also write variables create `.env` file.

    ```env
    github_token=
    github_username=
    bot_token=
    chat_id=
    ```

    You can generate GitHub API token from [settings page](https://github.com/settings/tokens/new). **do not check** any checkbox for read-only access.

    `chat_id` is not telegram username. find `message.chat.id` field using [`/getUpdates` Telegram bot API](https://core.telegram.org/bots/api#getupdates).

    If you are unfamiliar reading the Telegram API documentation, get this by chat with [`@get_id_bot`](https://telegram.me/get_id_bot)

3. Install dependencies to `pip install requests`.

    If you want to reference environment variables from `.env`, install `python-dotenv` from pip.

4. run `python run.py` every day.

## License

_commit-telegram-bot_ is primarily distributed under the terms of the MIT License. see [LICENSE](./LICENSE) for details.
