from linebot.v3.messaging import ApiClient, MessagingApi, ReplyMessageRequest, TextMessage, Configuration

from app.config import channel_access_token


def handle_text_message(event):
    configuration = Configuration(access_token=channel_access_token)
    with ApiClient(configuration) as api_client:
        messaging_api = MessagingApi(api_client)
        messaging_api.reply_message(
            ReplyMessageRequest(
                replyToken=event.reply_token,
                notificationDisabled=None,
                messages=[
                    TextMessage(
                        text=event.message.text,
                        # quoteToken=event.message.quote_token,
                        quoteToken=None,
                        quickReply=None)
                ],
            ))
