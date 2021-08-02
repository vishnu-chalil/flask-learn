from flask import Blueprint

blueprint = Blueprint(
    'close_out_blueprint',
    __name__,
    url_prefix='/close_out',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import eHDBS.user.routes #moga: F401