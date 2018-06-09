#!/bin/sh

# telegram configuration
while [ -z "$bot_token" ]
do
    read -p "Please enter Telegram bot token : " bot_token
done

while [ -z "$tele_id" ]
do
    read -p "Please check your id in https://telegram.me/userinfobot. user id : " tele_id
done

# github configuration
while [ -z "$username" ]
do
    read -p "GitHub username : " username
done

while [ -z "$gh_token" ]
do
    read -p "GitHub token : " gh_token
done

touch config.json

cat << EOF > config.json
{
	"bot_token":"$bot_token",
	"tele_id":"$tele_id",
	"username":"$username",
	"gh_token":"$gh_koken"
}
EOF

echo "\n\nDone."
