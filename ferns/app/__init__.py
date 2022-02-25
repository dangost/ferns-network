from flask import Flask

from ferns.app.app_config import Config
from ferns.routes import main_page


def create_app(config: Config) -> Flask:
    """
    1. Register all blueprints
    2. Initialize database
    3. Initialize other things for service
    4. app.run()
    :param config: init from .env or json file service settings
    :return: Flask app
    """
    app = Flask(__name__)

    app.register_blueprint(main_page)

    return app


