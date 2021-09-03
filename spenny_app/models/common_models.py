import enum

# third party imports
from sqlalchemy import (
    Column,
    text,
)


from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql import func


class DatetimeMixin(object):
    """
    common mixin class for datetime
    """

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )


class UserInvitationStatusType(enum.Enum):
    """
    Select type of status for MC Users

    At the moment we have added temperory option-data that can be changed as needed in the future
    """

    invited = "Invited"
    registered = "Registered"