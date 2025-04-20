from flask import Blueprint, request, current_app, abort
from linebot.v3.exceptions import InvalidSignatureError

from app.webhook_handlers.line_handler import handler

line_webhook_bp = Blueprint("line_webhook", __name__, url_prefix="/api/webhooks/line")


@line_webhook_bp.route("/message", methods=["POST"])
def message():
    signature = request.headers.get('X-Line-Signature', '')
    body = request.get_data(as_text=True)
    current_app.logger.info(f"[LINE] Webhook body: {body}")
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"
