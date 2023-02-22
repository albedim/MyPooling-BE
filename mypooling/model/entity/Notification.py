from mypooling.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 22/02/23
# Created at: 22:14
# Version: 1.0.0
# Description: This is the class for the notification entity
#


class Notification(sql.Model):
    __tablename__ = 'notifications'
    notification_id: int = sql.Column(sql.Integer, primary_key=True)
    receiver_id: int = sql.Column(sql.Integer, nullable=False)
    body: str = sql.Column(sql.String(240), nullable=False)
    seen: bool = sql.Column(sql.Boolean, nullable=False)

    def __init__(self, receiver_id, body):
        self.receiver_id = receiver_id
        self.body = body
        self.seen = False

    def toJson(self):
        return {
            'notification_id': self.notification_id,
            'receiver_id': self.receiver_id,
            'body': self.body,
            'seen': self.seen
        }

    def toJson_User(self, user):
        return {
            'notification_id': self.notification_id,
            'receiver_id': self.receiver_id,
            'body': self.body,
            'seen': self.seen,
            'receiver': user
        }