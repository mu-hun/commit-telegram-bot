#!/bin/sh

# telegram configuration
while [[ -z "$token" ]]
do
    read -p "Please enter Telegram bot TOKEN : " token
done

while [[ -z "$tele_id" ]]
do
    read -p "NOTE : please check your id to https://telegram.me/userinfobot \n Please enter Telegram user id : " tele_id
done

# github configuration
while [[ -z "$username" ]]
do
    read -p "Github username : " username
done

while [[ -z "$password" ]]
do
    read -s -p "Github password : " password
done

touch config.ini

cat << EOF > config.ini
[telegram]
token: $token
tele_id: $tele_id

[github]
username: $username
password: $password
EOF

echo "\n\nDone."