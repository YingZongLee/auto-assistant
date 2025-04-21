import logging

from flask import Flask

from app.routes.webhooks import webhook_blueprints


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt="%(asctime)s [%(process)d] %(levelname)-5s --- [%(threadName)s] %(name)-40s : %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S.%f"
    )
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    for bp in webhook_blueprints:
        app.register_blueprint(bp)
    return app
