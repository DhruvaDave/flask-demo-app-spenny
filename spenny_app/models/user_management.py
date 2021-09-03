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


class TblUsers(DatetimeMixin, handler.Base):
    """
    SQL Alchemy Model for - Users
    """

    __tablename__ = "tbl_users"
    user_id = Column(
        Integer, nullable=False, primary_key=True, unique=True, autoincrement=True
    )
    firstname = Column(String(64), nullable=False)
    lastname = Column(String(64), nullable=False)
    email = Column(String(256), nullable=False, unique=True)
    phone = Column(String(256), nullable=False)
    password_hash = Column(VARBINARY(64))
    display_language = Column(String(32), server_default="en-us")
    status = Column(String(124))
    temporary_password = Column(Boolean, server_default=expression.false())
    last_login_at = Column(TIMESTAMP)
    password_reset_id = Column(String(64))
    password_reset_at = Column(TIMESTAMP)
    is_deleted = Column(Boolean, server_default=expression.false())

    def __repr__(self):
        return "<TblUsers %r>" % (self.email)

    def to_json(self):
        return {
            'mc_user_id': self.user_id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'phone': self.phone,
            'display_language': self.display_language,
            'status': self.status.value if self.status else None,
            'created_by': self.created_by,
            'modified_by': self.modified_by
        }
