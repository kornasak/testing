import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

class Config:
    FLASK_APP = os.environ.get("FLASK_APP")
    TITLE = os.environ.get("TITLE")
    VERSION = os.environ.get("VERSION")
    DESCRIPTION = os.environ.get("DESCRIPTION")
    DEBUG = True
    SWAGGER_SUPPORTED_SUBMIT_METHODS = ["get", "post"]
    CONFIG_DOC = os.environ.get("DOC")
    DOC = True if CONFIG_DOC == 'true' else False
    # DB_URL = os.environ.get("MYSQL_URL")
    # GBP_GET_QRCODE_URI = os.environ.get("GBP_GET_QRCODE_URI")
    # GBP_WITHDRAW_URI = os.environ.get("GBP_WITHDRAW_URI")
    # GBP_GET_QRCODE_TOKEN = os.environ.get("GBP_GET_QRCODE_TOKEN")
    # GBP_WITHDRAW_TOKEN = os.environ.get("GBP_WITHDRAW_TOKEN")
    # GBP_CALLBACK_URL = os.environ.get("GBP_CALLBACK_URL")
    # MAX_EXPIRE = os.environ.get("MAX_EXPIRE")
    # MAX_EXPIRE_UNIT = os.environ.get("MAX_EXPIRE_UNIT")
