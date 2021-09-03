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


class TblFollwers(DatetimeMixin, handler.Base):
    """
    SQL Alchemy Model for - Followes
    """

    __tablename__ = "tbl_follwers"
    follwer_id = Column(
        Integer, nullable=False, primary_key=True, unique=True, autoincrement=True
    )
    user_id_fk = Column(Integer, ForeignKey("tbl_users.user_id"))
    follows_user_id_fk = Column(Integer, ForeignKey("tbl_users.user_id"))

    def __repr__(self):
        return "<TblFollwers %r>" % (self.follwer_id)

    def to_json(self):
        return {
            'follwer_id': self.follwer_id,
            'user_id_fk': self.user_id_fk,
            'follows_user_id_fk': self.follows_user_id_fk
        }
