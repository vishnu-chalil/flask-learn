from flask import Blueprint

blueprint = Blueprint(
    'base_visits_blueprint',
    __name__,
    url_prefix='/base_visits',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import edbhs.user.routes #moga: F401