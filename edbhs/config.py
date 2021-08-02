from os import environ


class Config(object):
    SQLALCHEMY_DATABASE_URI = environ.get(
        'edbhs_databse',
        'sqlite:///database.sqlite3?check_same_thread=False'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DB_SERVER = '192.168.1.30'


class DebugConfig(Config):
    DEBUG = True
    SECRET_KEY = environ.get(
        'edbhs_SECRET_KEY', 'passoword'
    )


class ProductionConfig(Config):
    DEBUG = False
    DB_SERVER = '192.168.1.21'
    SECRET_KEY = environ.get(
        'edbhs_SECRET_KEY', 'passoword'
    )

    VAULT_ADDRESS = environ.get('VAULT_ADDRESS')
    VAULT_TOKEN = environ.get('VAULT_TOKEN')


class TestingConfig(Config):
    DEBUG = False
    DB_SERVER = '127.0.0.1'
    SECRET_KEY = environ.get(
        'edbhs_SECRET_KEY', 'passoword'
    )
    TESTING = True
    DATABASE_URI = 'sqlite:///memory:'


app_config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
    'Testing': TestingConfig,

}
