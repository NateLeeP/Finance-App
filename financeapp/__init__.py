from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os
import logging

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'users.login' # Login manager knows where to redirect when login needed
login.login_message_category = 'info'
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger(__name__).setLevel(logging.INFO)

from financeapp.chart.routes import chart_blueprint
from financeapp.portfolio.routes import portfolio_blueprint
from financeapp.users.routes import users
# from financeapp.test.routes import test_blueprint

app.register_blueprint(chart_blueprint)
app.register_blueprint(portfolio_blueprint)
app.register_blueprint(users)
# app.register_blueprint(test_blueprint)


#from financeapp import routes, models
