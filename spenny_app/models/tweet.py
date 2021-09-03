from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    VARBINARY,
    JSON,
    Enum)
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.orm import relationship

# local imports
from spenny_app.config.db_handler import handler
from sqlalchemy.sql import expression
from spenny_app.models.common_models import DatetimeMixin


class TblTweets(DatetimeMixin, handler.Base):
    """
    SQL Alchemy Model for - Tweets
    """

    __tablename__ = "tbl_tweets"
    tweet_id = Column(
        Integer, nullable=False, primary_key=True, unique=True, autoincrement=True
    )
    tweet_description = Column(String(140), nullable=False)
    user_id_fk = Column(Integer, ForeignKey("tbl_users.user_id"))
    is_deleted = Column(Boolean, server_default=expression.false())


    def __repr__(self):
        return "<TblTweets %r>" % (self.tweet_id)

    def to_json(self):
        return {
            'tweet_id': self.tweet_id,
            'tweet_description': self.tweet_description,
            'user_id_fk': self.user_id_fk,
            'is_deleted': self.is_deleted
        }
