import logging
from flask import Blueprint

from spenny_app.common.forms.follower_management_forms import FollwerForm
from spenny_app.services.follower_management_service.follower_management_data import (
    FollowersData
)
from spenny_app.utils.session_management import have_logged_in


logger = logging.getLogger(__name__)

followers_management_process = Blueprint("followers_management_process", __name__)


@followers_management_process.route("", methods=["POST"])
@have_logged_in()
def add_follower():
    """
        Add follower
    """
    logger.info('Incoming request for add follower.')
    form = FollwerForm()
    response = FollowersData.follwer_add(form)
    return response



