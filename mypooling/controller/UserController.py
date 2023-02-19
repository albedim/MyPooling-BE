from flasgger import swag_from
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_cors import cross_origin
from mypooling.service.UserService import UserService
from mypooling.utils.Utils import Utils


user: Blueprint = Blueprint('UserController', __name__, url_prefix=Utils.getURL('user'))


@user.route("/signin", methods=['POST'])
@cross_origin()
@swag_from('./docs/user/signin.yaml')
def signin():
    return UserService.signin(request.json)


@user.route("/session_check", methods=['GET'])
@cross_origin()
@jwt_required()
@swag_from('./docs/user/session_check.yaml')
def isExpired():
    return get_jwt_identity()


@user.route("/signup", methods=['POST'])
@cross_origin()
@swag_from('./docs/user/signup.yaml')
def signup():
    return UserService.signup(request.json)




