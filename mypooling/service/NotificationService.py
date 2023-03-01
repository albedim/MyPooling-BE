from flask import jsonify

from mypooling.model.entity.Notification import Notification
from mypooling.model.entity.User import User
from mypooling.model.repository.NotificationRepository import NotificationRepository
from mypooling.model.repository.UserRepository import UserRepository
from mypooling.service.user.UserService import UserService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 24/02/23
# Created at: 23:14
# Version: 1.0.0
# Description: This is the class for the user notification service
#


class NotificationService():

    @classmethod
    def notify(cls, notificationType, receiverId):
        if notificationType == 'RIDE_ADDED':
            NotificationRepository.notify(
                receiverId,
                Constants.RIDE_ADDED.replace("{username}", UserRepository.getUserById(receiverId).username)
            )

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