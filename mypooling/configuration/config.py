from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils
from resources.config import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config['username'] + ':' + config['password'] + '@' + config['host'] + '/' + config['db-name']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config["JWT_SECRET_KEY"] = "super-secret"
sql = SQLAlchemy(app)


@app.errorhandler(404)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_NOT_FOUND, 404), 404


@app.errorhandler(405)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_METHOD_NOT_ALLOWED, 405), 405


@app.errorhandler(500)
def page_not_found(e):
    return Utils.createWrongResponse(False, Constants.PAGE_UNKNOWN_ERROR, 500), 500