from mypooling.model.entity.User import User
from mypooling.model.repository.UserRepository import UserRepository
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils


class UserService():

    @classmethod
    def signin(cls, request: dict):
        try:
            user: User = UserRepository.signin(
                request['email'],
                Utils.hash(request['password'])
            )
            if user is not None:
                return Utils.createSuccessResponse(True, user.user_id)
            else:
                return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def exists(cls, email, username) -> bool:
        return UserRepository.existsByEmail(email) > 0 or UserRepository.existsByUsername(username) > 0

    @classmethod
    def getUser(cls, userId) -> dict:
        return UserRepository.getUser(userId).toJson()

    @classmethod
    def signup(cls, request: dict):
        try:
            if not cls.exists(request['email'], request['username']):
                UserRepository.signup(
                    request['username'],
                    request['name'],
                    request['email'],
                    Utils.hash(request['password'])
                )
                return Utils.createSuccessResponse(True, Constants.CREATED)
            else:
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 403)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)