import logging

from spenny_app.models.follower import TblFollwers
from sqlalchemy import desc
from spenny_app.config.db_handler import handler

from spenny_app.models.tweet import TblTweets

logger = logging.getLogger(__name__)

db_session = handler.db_session


class TweetRepo:

    @staticmethod
    def create_tweet(tweet_data):
        """
        Create tweet
        """

        db_session.add(TblTweets(**tweet_data))
        db_session.flush()
        db_session.commit()

        return True

    @staticmethod
    def fetch_tweet_by_user_id(user_id, offset, limit):
        """
        Fetch tweet
        """

        query = TblTweets.query\
            .filter_by(user_id_fk=user_id)

        total = query.count()
        tweet_data = (
            query.order_by(desc('created_at')).offset(offset).limit(limit).all()
        )
        return total, tweet_data

    @staticmethod
    def fetch_tweet_by_user_followers(user_id, offset, limit):
        """
        Fetch followers tweet
        """

        follower_ids = TblFollwers.query.with_entities(TblFollwers.follows_user_id_fk). \
            filter(TblFollwers.user_id_fk == user_id)

        query = TblTweets.query\
            .filter(TblTweets.user_id_fk.in_(follower_ids.subquery()))

        total = query.count()
        tweet_data = (
            query.order_by(desc('created_at')).offset(offset).limit(limit).all()
        )
        return total, tweet_data
