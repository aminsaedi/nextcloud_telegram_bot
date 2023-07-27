# nextcloud_telegram_bot

A simple telegram bot to upload any forwarded file to your WebDAV server

## Installation

1. Clone this repository
2. Install the requirements with `pip install -r requirements.txt`
3. Create a bot with the [BotFather](https://t.me/botfather) and copy the token
4. Create a .env file
5. Add the following lines to the .env file:

```
TELEGRAM_BOT_TOKEN=<your token>
WEBDAV_HOSTNAME=<your next cloud webDAV address>
WEBDAV_LOGIN=<your next cloud login>
WEBDAV_PASSWORD=<your next cloud password>
```

6. Run the bot with `python3 main.py`

## Docker

```
docker build -t nextcloud_telegram_bot .
docker run -d --name nextcloud_telegram_bot --restart always --env-file .env nextcloud_telegram_bot
```
