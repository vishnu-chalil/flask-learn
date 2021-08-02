from flask import Blueprint

blueprint = Blueprint(
    'scheduled_visits_blueprint',
    __name__,
    url_prefix='/users',
    template_folder='scheduled_visits',
    static_folder='static'
)
from .import routes

#import eHDBS.user.routes #moga: F401