import logging

import requests
from flask import jsonify

from app.config import slack_bot_token

logger = logging.getLogger(__name__)

def handle_verification(data):
    challenge = data.get("challenge")
    return jsonify({"challenge": challenge})


def handle_text_message(channel: str, text: str):
    try:
        response = requests.post(
            "https://slack.com/api/chat.postMessage",
            headers={
                "Authorization": f"Bearer {slack_bot_token}",
                "Content-Type": "application/json"
            },
            json={
                "channel": channel,
                "text": text
            })
        result = response.json()
        if not result['ok']:
            logger.warning(f"[SLACK] Failed to post message: {result}")
        else:
            logger.info(f"[SLACK] Posted message: {result}")
    except Exception as e:
        logger.exception(f"[SLACK] Error posting message: {e}")



