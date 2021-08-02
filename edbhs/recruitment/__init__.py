from flask import Blueprint

blueprint = Blueprint(
    'recruitment_blueprint',
    __name__,
    url_prefix='/recruitment',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import edbhs.user.routes #moga: F401