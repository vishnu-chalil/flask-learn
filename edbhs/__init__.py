from flask import Flask
from importlib import import_module
from flask_sqlalchemy import SQLAlchemy
from hvac import Client as VaultClient

db = SQLAlchemy(session_options={"expire_on_commit": False})


def register_blueprints(app):
    blueprints = {
        'base',
        'admin',
        'base_visits',
        'close_out',
        'follow_visits',
        'inclusion_criteria',
        'lab',
        'radiology',
        'recruitment',
        'scheduled_visits',
        'users'
    }
    for blueprint in blueprints:
        module = import_module(f'x.edbhs.{blueprint}')
        print(module.blueprint)
        app.register_blueprint(module.blueprint)
        print(blueprint)


def create_vault_client(app):
    return VaultClient(
        url=app.config('VAULT_ADDRESS'),
        token=app.config('VAULT_TOKEN')
    )


def configure_database(app):
    @app.before_first_request
    def create_default():
        db.create_all()


def create_app(path, config):
    app = Flask(__name__, static_folder='base/static')
    app.config.from_object(config)
    app.production = not app.config['DEBUG']
    app.path = path
    register_blueprints(app)
    configure_database(app)
    if app.production:
        app.vault_client = create_vault_client(app)
    return app
