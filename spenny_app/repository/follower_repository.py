import logging

from spenny_app.config.db_handler import handler
from spenny_app.models.follower import TblFollwers

logger = logging.getLogger(__name__)

db_session = handler.db_session


class FollwerRepo:

    @staticmethod
    def create_follower(tweet_data):
        """
        Create tweet
        """

        db_session.add(TblFollwers(**tweet_data))
        db_session.flush()
        db_session.commit()

        return True

    @staticmethod
    def fetch_follower(user_id, follows_user_id):
        """
            Fetch follower
        """
        user_follower_data = (
            TblFollwers.query\
                .filter(TblFollwers.user_id_fk == user_id)
                .filter(TblFollwers.follows_user_id_fk == follows_user_id)
                .first()
        )
        return user_follower_data