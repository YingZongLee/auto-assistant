from app.routes.webhooks.line_webhook import line_webhook_bp
from app.routes.webhooks.slack_webhook import slack_webhook_bp

webhook_blueprints = [ line_webhook_bp, slack_webhook_bp]