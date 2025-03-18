import configparser
import ssl
import sys

import certifi
import urllib3
from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent, )

# ----------------------------------------------------------------
# 1) READ CONFIG/ENV
# ----------------------------------------------------------------
config = configparser.ConfigParser()
config.read('config.ini')

channel_secret = config['Line'].get('CHANNEL_SECRET')
channel_access_token = config['Line'].get('CHANNEL_ACCESS_TOKEN')

if not channel_secret:
    print("Error: 'CHANNEL_SECRET' not found in [Line] section of config.ini.")
    sys.exit(1)
if not channel_access_token:
    print("Error: 'CHANNEL_ACCESS_TOKEN' not found in [Line] section of config.ini.")
    sys.exit(1)

# Prepare the webhook handler and the API configuration
handler = WebhookHandler(channel_secret)
# 强制 urllib3 使用 certifi 证书
urllib3.disable_warnings()  # 可选：暂时禁用 SSL 警告（仅用于调试）
http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
ssl_context = ssl.create_default_context(cafile=certifi.where())
configuration = Configuration(access_token=channel_access_token)

# ----------------------------------------------------------------
# 2) FLASK APP
# ----------------------------------------------------------------
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Hello World!"


@app.route("/callback", methods=["POST"])
def callback():
    # 1. Get X-Line-Signature
    signature = request.headers.get('X-Line-Signature', '')
    # 2. Get request body
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # 3. Handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        # If signature check fails, this means the request is not from LINE
        abort(400)

    return "OK"


# ----------------------------------------------------------------
# 3) HANDLE EVENTS
# ----------------------------------------------------------------
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    """Reply with the same text the user sends."""
    with ApiClient(configuration) as api_client:
        api_client.rest_client.pool_manager.connection_pool_kw['ssl_context'] = ssl_context
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message(
            ReplyMessageRequest(
                replyToken=event.reply_token,
                notificationDisabled=None,
                messages=[
                    TextMessage(
                        text=event.message.text,
                        quoteToken=None,
                        quickReply=None)
                ],
            ))


# ----------------------------------------------------------------
# 4) RUN THE APP
# ----------------------------------------------------------------
if __name__ == "__main__":
    # Make sure to use a port your environment expects.
    # If you run locally, just use 5000 or 5001.
    # And for LINE Bot, you'll typically tunnel via ngrok or similar.
    app.run(debug=True, port=5001)
