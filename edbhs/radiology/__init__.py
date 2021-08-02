from flask import Blueprint

blueprint = Blueprint(
    'radiology_blueprint',
    __name__,
    url_prefix='/radiology',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import edbhs.user.routes #moga: F401