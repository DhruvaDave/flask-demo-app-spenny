"""
HTTP Exception 
"""
import logging
 
from spenny_app.common.constants import DEFAULT_HTTP_ERROR_CODE, DEFAULT_ERROR_CODE, DEFAULT_HTTP_ERROR_MESSAGE
logger = logging.getLogger(__name__)


class HttpException(Exception):
    def __init__(self, message=DEFAULT_HTTP_ERROR_MESSAGE, code=DEFAULT_ERROR_CODE, http_code=DEFAULT_HTTP_ERROR_CODE):
        print("----------code-----",code,"------htttp---",http_code)
        self.code = code
        self.message = message
        self.http_code = http_code
        super().__init__(message)