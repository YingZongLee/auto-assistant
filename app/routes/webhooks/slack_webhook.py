from flask import Blueprint, request, current_app

from app.webhook_handlers.slack_handler import slack_handler
from app.service.slack_service import handle_verification

slack_webhook_bp = Blueprint("slack_webhook", __name__, url_prefix="/api/webhooks/slack")


@slack_webhook_bp.route("/message", methods=["POST"])
def message():
    data = request.get_json()
    current_app.logger.info(f"[SLACK] Webhook body: {data}")
    if data.get("type") == "url_verification":
        return handle_verification(data)
    slack_handler.handle(request)
    return "", 200
