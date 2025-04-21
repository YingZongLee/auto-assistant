from linebot.v3 import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent

from app.config import channel_secret
from app.service.line_service import handle_text_message

handler = WebhookHandler(channel_secret)


@handler.add(MessageEvent, message=TextMessageContent)
def on_message(event):
    handle_text_message(event)
