from datetime import timedelta

from flask_jwt_extended import create_access_token, jwt_required

from mypooling.model.entity.User import User
from mypooling.model.repository.UserRepository import UserRepository
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user service
#


class UserService():

    @classmethod
    def signin(cls, request: dict):
        try:
            user: User = UserRepository.signin(
                request['email'],
                Utils.hash(request['password'])
            )
            if user is not None:
                return Utils.createSuccessResponse(True, create_access_token(
                    identity=user.toJson(), expires_delta=timedelta(weeks=4)))
            else:
                return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def exists(cls, email, username) -> bool:
        return UserRepository.existsByEmail(email) > 0 or UserRepository.existsByUsername(username) > 0

    @classmethod
    def getUser(cls, userId) -> dict:
        return UserRepository.getUserById(userId).toJson()

    @classmethod
    def signup(cls, request: dict):
        try:
            if not cls.exists(request['email'], request['username']):
                UserRepository.signup(
                    request['username'],
                    request['name'],
                    request['email'],
                    request['age'],
                    request['bio'],
                    request['place'],
                    Utils.hash(request['password'])
                )
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 409), 409
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def createForgottenPasswordToken(cls, email):
        user: User = UserRepository.getUserByEmail(email)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            token: str = Utils.createLink(140)
            UserRepository.createForgottenPasswordToken(user, token)
            Utils.sendPasswordForgottenEmail(user.name, user.email, token)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = UserRepository.getUserByPasswordForgottenToken(token)
        if user is None:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404
        else:
            return Utils.createSuccessResponse(True, user.user_id), 200

    @classmethod
    def changePassword(cls, request):
        try:
            UserRepository.changePassword(request['user_id'], Utils.hash(request['new_password']))
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def changeData(cls, request: dict):
        try:
            UserRepository.changeData(
                request['user_id'],
                request['username'],
                request['name'],
                request['email'],
                request['age'],
                request['bio'],
                request['place'],
                Utils.hash(request['password'])
            )
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400
