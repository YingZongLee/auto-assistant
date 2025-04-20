from flask import Flask

from app.routes.webhooks import webhook_blueprints


def create_app():
    app = Flask(__name__)
    for bp in webhook_blueprints:
        app.register_blueprint(bp)
    return app
