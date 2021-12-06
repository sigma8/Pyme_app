from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_bootstrap import Bootstrap
from flask_admin import Admin



db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
bootstrap = Bootstrap()
admin = Admin()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)
    admin.init_app(app)




    #Registrando blueprint errors
    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    #Registrando blueprint auth
    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    #Registrando blueprint index
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #Registrando blueprint index
    #from app.administrator import bp as admin_bp
    #app.register_blueprint(admin_bp, url_prefix='/administrator')

    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
            file_handler = RotatingFileHandler('logs/blog.log', maxBytes=10240, backupCount=10)
            file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Blog Log')

    return app

from app import models
