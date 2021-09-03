import logging
from flask import Blueprint, request

from spenny_app.common.forms.tweet_management_forms import TweetForm
from spenny_app.services.user_management_service.user_management_data import (
    UsersData,
)
from spenny_app.services.tweet_management_service.tweet_management_data import (
    TweetsData,
)
from spenny_app.utils.session_management import have_logged_in

logger = logging.getLogger(__name__)

tweet_management_process = Blueprint("tweet_management_process", __name__)


@tweet_management_process.route("", methods=["POST"])
@have_logged_in()
def tweets():
    """
        Post tweet
    """
    logger.info('Incoming request for post tweet.')
    form = TweetForm()
    response = TweetsData.tweet_add(form)
    return response


@tweet_management_process.route("", methods=["GET"])
@have_logged_in()
def get_tweets():
    """
        Get persoal tweets
    """
    logger.info('Incoming request for get personal tweets.')
    query_params = request.args
    response = TweetsData.get_user_tweets(query_params)
    return response

@tweet_management_process.route("/followers", methods=["GET"])
@have_logged_in()
def get_followers_tweets():
    """
        Get followers tweet
    """
    logger.info('Incoming request for get follower\'s tweets.')
    query_params = request.args
    response = TweetsData.get_followers_tweets(query_params)
    return response
