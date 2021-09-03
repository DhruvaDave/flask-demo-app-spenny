import json
import logging
from sqlalchemy import exc
from flask import session, jsonify
from sqlalchemy.sql.functions import user

from spenny_app.common import constants
from spenny_app.exceptions.http_exception import HttpException


from spenny_app.models.user_management import TblUsers
from spenny_app.repository.follower_repository import FollwerRepo


from spenny_app.common import messages
from spenny_app.utils.session_management import get_current_user_id

logger = logging.getLogger(__name__)


class FollowersData:

    @staticmethod
    def follwer_add(form):
        """
            Add follower
        """
        if not form.validate_on_submit():
            logging.debug(messages.INVALID_FORM_MESSAGE, form.errors)
            raise HttpException(messages.INVALID_FORM_MESSAGE,
                                constants.BAD_REQUEST, 400)
      
        
        user_id = get_current_user_id()
        logging.info(f'User id: {user_id}')
        user_follower_data = FollwerRepo.fetch_follower(user_id, form.follows_user_id.data)
        if user_follower_data:
            return jsonify(
            {
                "code": constants.ENTITY_EXISTS,
                "message": "Already following selected user."
            }
        )
        data = {
            "user_id_fk": user_id,
            "follows_user_id_fk": form.follows_user_id.data,
        }
        FollwerRepo.create_follower(data)
        logger.info('Follower added successfully')
       

        return jsonify(
            {
                "code": constants.SUCCESS,
                "message": "Follower Added Successfully"
            }
        )

    