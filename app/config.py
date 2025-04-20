import configparser
import sys

from flask import current_app

config = configparser.ConfigParser()
config.read('config.ini')

channel_secret = config['Line'].get('CHANNEL_SECRET')
channel_access_token = config['Line'].get('CHANNEL_ACCESS_TOKEN')

if not channel_secret or not channel_access_token:
    current_app.logger.error("Error: Missing LINE credentials in config.ini.")
    sys.exit(1)

slack_bot_token = config["Slack"]["BOT_TOKEN"]
slack_signing_secret = config["Slack"]["SIGNING_SECRET"]

if not slack_bot_token or not slack_signing_secret:
    current_app.logger.error("Error: Missing Slack credentials in config.ini.")
    sys.exit(1)
