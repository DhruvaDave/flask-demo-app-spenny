"""
    Main entry point of flask app
"""
import logging
from spenny_app import create_app

from spenny_app.config.db_handler import register_models
from spenny_app.config.app_config import CommonConfig
from spenny_app.log_utils import logger
import pathlib
import os

absolute_path = pathlib.Path(__file__).parent.absolute()
CONFIG_FILE = str(absolute_path) + "/spenny_app/config/logging.json"

logger.setup_logging(config_file=CONFIG_FILE)
logger = logging.getLogger("Spenny-App")

register_models()
app = create_app()

if __name__ == "__main__":
    logger.info("Initializing app ...")
    os.system("alembic upgrade head")
    app.run(host="0.0.0.0", port=CommonConfig.app_port, debug=CommonConfig.debug)
