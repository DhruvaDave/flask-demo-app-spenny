import logging
import wtforms_json

from flask_wtf import Form
from wtforms.validators import DataRequired
from wtforms import IntegerField

logger = logging.getLogger(__name__)

wtforms_json.init()


class FollwerForm(Form):
    follows_user_id = IntegerField(validators=[DataRequired()])
