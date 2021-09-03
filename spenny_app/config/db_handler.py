"""
    DB Handler used across project
"""
import logging
from spenny_app.utils.db_utils import MySQLHandler 
from spenny_app.config.db_config import DBConfig

logger = logging.getLogger("DB-Handler")

db_passcode = DBConfig.password.replace("%", "%%")
handler = MySQLHandler(
    DBConfig.host,
    DBConfig.user,
    DBConfig.password,
    DBConfig.port,
    DBConfig.dbname,
    DBConfig.pool_size,
)


def register_models():
    """
    Model initialization
    """
    logger.info("Initializing MySQL handler ... ")
    handler.initialize_db()

    # pylint: disable=W0611,C0415
    # note: Ignoring 'Import outside toplevel' as related to system trace
    # DATABASE TABLES WILL BE CREATED ONLY FOR MODELS IMPORTED HERE
    from spenny_app.models.user_management import TblUsers
    from spenny_app.models.tweet import TblTweets
    from spenny_app.models.follower import TblFollwers

    handler.Base.metadata.create_all(bind=handler.engine)
