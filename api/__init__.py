import logging, os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from importlib import import_module

## Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

####################
## GLOBAL
db_api = SQLAlchemy()
#login_manager = LoginManager()
jwt = None

####################
## APP

##  creating Flask app :
def create_app():
    logging.info('⌛ Creating Flask app')
    app = Flask(__name__)
    
    return app

## Config
def config_app(app, flask_key, jwt_key):
    logging.info('⌛ Configuration')
    app.debug = True
    app.config.update(
        TESTING=True,
        SECRET_KEY=flask_key,
        JWT_SECRET_KEY = jwt_key
    )

    global jwt 
    jwt = JWTManager(app)

    #login_manager.init_app(app)



## Blueprint
def register_blueprints(app):
    logging.info('⌛ Registering blueprints')

    # Registering Auth module
    auth_module = import_module('api.auth.routes')
    app.register_blueprint(auth_module.blueprint)

    # Registering Notifier module
    notifier_module = import_module('api.notifier.routes')
    app.register_blueprint(notifier_module.notifier_blueprint)


####################
## DATABASE

## Config DB
def config_db(app):
    logging.info('⌛ Configuration of the database')
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:////'+ os.path.abspath(os.getcwd()) + '/db.sqlite3',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

## Init DB
def init_db(app):
    logging.info('⌛ Preparing the database')

    global db_api

    db_api.init_app(app)

    @app.before_first_request
    def initialize_database():
        logging.debug('🌟 Init database')
        db_api.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        logging.debug('💥 Killing session')
        db_api.session.remove()

####################
## GENERAL

def init_api(flask_key, jwt_key):
    logging.info('⌛ Starting...')

    ## app
    app = create_app()
    config_app(app, flask_key, jwt_key)

    # db
    config_db(app)
    init_db(app)

    register_blueprints(app)

    logging.info('✅ App started and configured')
    
    return app

