import configparser
import os
import sys

from flask import current_app

config = configparser.ConfigParser()
config.read('config.ini')

def get_config(key, section):
    return os.environ.get(key) or config.get(section, key, fallback=None)

channel_secret = get_config("LINE_CHANNEL_SECRET", "Line")
channel_access_token = get_config("LINE_CHANNEL_ACCESS_TOKEN", "Line")

if not channel_secret or not channel_access_token:
    try:
        current_app.logger.error("LINE config missing: LINE_CHANNEL_SECRET or LINE_CHANNEL_ACCESS_TOKEN")
    except RuntimeError:
        print("LINE config missing: LINE_CHANNEL_SECRET or LINE_CHANNEL_ACCESS_TOKEN", file=sys.stderr)
    sys.exit(1)

slack_bot_token = get_config("SLACK_BOT_TOKEN", "Slack")
slack_signing_secret = get_config("SLACK_SIGNING_SECRET", "Slack")

if not slack_bot_token or not slack_signing_secret:
    try:
        current_app.logger.error("Slack config missing: BOT_TOKEN or SIGNING_SECRET")
    except RuntimeError:
        print("Slack config missing: BOT_TOKEN or SIGNING_SECRET", file=sys.stderr)
    sys.exit(1)
