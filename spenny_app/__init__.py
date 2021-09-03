"""
    Flask app intialization
"""
import logging
from flask import Flask, g, request
from spenny_app.config.app_config import CommonConfig 

logger = logging.getLogger(__name__)


def create_app():
    """
    Flask factory styling for creating app
    """
    # pylint: disable=C0415
    # note: Ignoring 'Import outside toplevel' to avoid import while init

    from spenny_app.config.swagger import SwaggerConfig
    from spenny_app.routes.users import user_management_process
    from spenny_app.routes.tweets import tweet_management_process
    from spenny_app.routes.followers import followers_management_process

    # Define the WSGI application object
    app = Flask(__name__)

    # DEBUG ONLY!
    app.config["WTF_CSRF_ENABLED"] = CommonConfig.wtf_csrf
    app.config["SECRET_KEY"] = CommonConfig.app_secret_key

    @app.route("/")
    def home():
        return "We are working for new feature development! Please come back later!"

    @app.route('/favicon.ico')
    def favicon():
        # To avoid 404 error
        return {}, 200



    # pylint: disable=W0613
    # note: Ignoring Unused argument 'resp_or_exc' as it's related to app
    # @app.teardown_appcontext
    # def cleanup(resp_or_exc):
    #     handler.db_session.remove()

    # Register the blueprint here
    
    app.register_blueprint(
        SwaggerConfig.SWAGGERUI_BLUEPRINT, url_prefix=SwaggerConfig.SWAGGER_URL
    )
    app.register_blueprint(user_management_process, url_prefix="/api/v1/users")
    app.register_blueprint(tweet_management_process, url_prefix="/api/v1/tweets")
    app.register_blueprint(followers_management_process, url_prefix="/api/v1/followers")
   

    return app
