from flask import Blueprint

blueprint = Blueprint(
    'follow_visits_blueprint',
    __name__,
    url_prefix='/follow_visits',
    template_folder='templates',
    static_folder='static'
)
from .import routes

#import edbhs.user.routes #moga: F401