from flask import jsonify

from mypooling.model.entity.Notification import Notification
from mypooling.model.entity.User import User
from mypooling.model.repository.NotificationRepository import NotificationRepository
from mypooling.model.repository.UserRepository import UserRepository
from mypooling.service.user.UserService import UserService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils


class NotificationService():

    @classmethod
    def notify(cls, request):
        try:
            body: str = ""
            if request['body'] == 'RIDE_ADDED':
                body = Constants.RIDE_ADDED.replace("{username}", UserRepository.getUserById(request['receiver_id']).username)
            else:
                return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400
            NotificationRepository.notify(request['receiver_id'], body)
            return Utils.createSuccessResponse(True, Constants.CREATED), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def getAll(cls, userId):
        notifications: list[Notification] = NotificationRepository.getAll(userId)
        result: list = []
        for notification in notifications:
            user: dict = UserService.getUser(notification.receiver_id)
            result.append(notification.toJson_User(user))
        return jsonify(result)

    @classmethod
    def markAsSeen(cls, notificationId):
        NotificationRepository.markAsSeen(notificationId)
        return Utils.createSuccessResponse(True, Constants.CREATED), 200