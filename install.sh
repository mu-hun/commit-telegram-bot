#!/bin/sh

# install apex to deploy to AWS Lambda
apex=apex

if ! apex_loc="$(type -p "$apex")" || [ -z "$apex" ]; then
    echo "Installing apex ..."
    curl https://raw.githubusercontent.com/apex/apex/master/install.sh | sh
else
    echo "Apex is already installed."
fi

echo "\n"

# slack configuration
while [[ -z "$telegram_token" ]]
do
    read -p "Telegram bot TOKEN : " telegram_token
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

touch config/github.ini
touch config/telegram.ini

cat << EOF > config/telegram.ini
[telegram]
telegram_token: $telegram_token
EOF

cat << EOF > config/github.ini
[github]
username: $username
password: $password
EOF

echo "\n\nDone."