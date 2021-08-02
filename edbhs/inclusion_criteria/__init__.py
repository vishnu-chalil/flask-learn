from flask import Blueprint

blueprint = Blueprint(
    'inclusion_criteria_blueprint',
    __name__,
    url_prefix='/inclusion_criteria',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import eHDBS.user.routes #moga: F401