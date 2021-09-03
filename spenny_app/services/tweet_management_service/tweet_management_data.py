import json
import logging

from flask import jsonify

from spenny_app.common import constants
from spenny_app.exceptions.http_exception import HttpException

from spenny_app.repository.tweet_repository import TweetRepo

from spenny_app.common import messages
from spenny_app.utils.session_management import get_current_user_id
from spenny_app.utils.pagination import get_pagination

logger = logging.getLogger(__name__)


class TweetsData:

    @staticmethod
    def tweet_add(form):
        if not form.validate_on_submit():
            logging.debug(messages.INVALID_FORM_MESSAGE, form.errors)
            raise HttpException(messages.INVALID_FORM_MESSAGE,
                                constants.BAD_REQUEST, 400)
              
        if len(form.tweet.data) > constants.TWEET_CHARACTER_LIMIT:
            return jsonify(
            {
                "code": constants.BAD_REQUEST,
                "message": f"You can tweet only upto {constants.TWEET_CHARACTER_LIMIT} characters."
            }
        )

        data = {
            "user_id_fk": get_current_user_id(),
            "tweet_description": form.tweet.data,
        }
        TweetRepo.create_tweet(data)
       
        return jsonify(
            {
                "code": constants.SUCCESS,
                "message": "Tweeted Successfully"
            }
        )

    @staticmethod
    def get_user_tweets(query_params):
               
        result = []
        user_id = get_current_user_id()

        offset, limit = get_pagination(query_params)

        total, tweets_data = TweetRepo.fetch_tweet_by_user_id(user_id, offset, limit)

        if total == 0:
            return jsonify({"code": constants.NO_ENTITY_FOUND,
                            "message": "No results found."})

        for data in tweets_data:
            result.append({
                "tweet": data.tweet_description,
                "user": data.user_id_fk,
                "tweet_id": data.tweet_id
            })

        return jsonify(
            {
                "code": constants.SUCCESS,
                "message": "Tweets Fetched Successfully",
                "result": result,
                "page": query_params.get('page_no'),
                "page_size": query_params.get('page_size'),
                "total_records": total
            }
        )
    
    @staticmethod
    def get_followers_tweets(query_params):
               
        result = []
        user_id = get_current_user_id()
        offset, limit = get_pagination(query_params)

        total, tweets_data = TweetRepo.fetch_tweet_by_user_followers(user_id, offset, limit)

        for data in tweets_data:
            result.append({
                "tweet": data.tweet_description,
                "user": data.user_id_fk,
                "tweet_id": data.tweet_id
            })

        return jsonify(
            {
                "code": constants.SUCCESS,
                "message": "Tweets Fetched Successfully",
                "result": result,
                "page": query_params.get('page_no'),
                "page_size": query_params.get('page_size'),
                "total_records": total
            }
        )
    