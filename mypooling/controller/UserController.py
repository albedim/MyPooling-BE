from flask import Blueprint, request
from flask_cors import cross_origin
from mypooling.service.UserService import UserService
from mypooling.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
def signin():
    return UserService.signin(request.json)


@user.route("/signup", methods=['POST'])
@cross_origin()
def signup():
    return UserService.signup(request.json)




