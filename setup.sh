#!/bin/sh

# telegram configuration
while [[ -z "$tele_token" ]]
do
    read -p "Please enter Telegram bot token : " tele_token
done

while [[ -z "$tele_id" ]]
do
    read -p "Please check your id in https://telegram.me/userinfobot \n Please enter Telegram user id : " tele_id
done

# github configuration
while [[ -z "$git_user" ]]
do
    read -p "GitHub Username : " git_user
done

while [[ -z "$git_pass" ]]
do
    read -s -p "GitHub Password : " git_pass
done

touch config.json

cat << EOF > config.json
{
	"tele_token":"$tele_token",
	"tele_id":"$tele_id",
	"git_user":"$git_user",
	"git_pass":"$git_pass"
}
EOF

echo "\n\nDone."
