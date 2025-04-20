from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler

from app.config import slack_bot_token, slack_signing_secret
from app.service.slack_service import handle_text_message

slack_bolt_app = App(token=slack_bot_token, signing_secret=slack_signing_secret)
slack_handler = SlackRequestHandler(slack_bolt_app)


@slack_bolt_app.event("message")
def on_message(body):
    text = body["event"]["text"]
    channel = body["event"]["channel"]
    handle_text_message(channel, text)
