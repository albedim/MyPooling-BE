from flasgger import swag_from
from flask import Blueprint, request
from flask_cors import cross_origin

from mypooling.service.FeedbackService import FeedbackService
from mypooling.service.NotificationService import NotificationService
from mypooling.utils.Utils import Utils


notification: Blueprint = Blueprint('NotificationService', __name__, url_prefix=Utils.getURL('notification'))


@notification.route("/mark_as_seen/<notificationId>", methods=['PUT'])
@cross_origin()
@swag_from('./docs/notification/mark_as_seen.yaml')
def markAsSeen(notificationId):
    return NotificationService.markAsSeen(notificationId)


@notification.route("/get/<userId>", methods=['GET'])
@cross_origin()
@swag_from('./docs/notification/get.yaml')
def get(userId: int):
    return NotificationService.getAll(int(userId))




