from flask_migrate import Migrate
from os import environ
from pathlib import Path
from sys import exit
from . import create_app, db
from .config import app_config_dict

get_config_mode = environ.get('edbhs_CONFIG_MODE', 'Debug')

try:
    config_mode = app_config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('invalid config mode')

app = create_app(Path.cwd, config_mode)

db.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    # manager.run()
    app.run()
