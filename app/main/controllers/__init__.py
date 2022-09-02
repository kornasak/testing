from flask_restplus import Api
from app.main.config import Config

# init
from .welcome.WelcomeController import api as Welcome

if Config.DOC:
    api = Api(
        title=Config.TITLE,
        version=Config.VERSION,
        description=Config.DESCRIPTION
    )
else:
    api = Api(
        title=Config.TITLE,
        version=Config.VERSION,
        description=Config.DESCRIPTION,
        doc=False
    )

# init
api.add_namespace(Welcome)