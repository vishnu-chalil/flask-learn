from flask import Blueprint

blueprint = Blueprint(
    'lab_blueprint',
    __name__,
    url_prefix='/lab',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import edbhs.user.routes #moga: F401