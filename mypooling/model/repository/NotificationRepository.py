from mypooling.configuration.config import sql
from mypooling.model.entity.Notification import Notification


class NotificationRepository():

    @classmethod
    def notify(cls, receiver_id, body):
        notification: Notification = Notification(receiver_id, body)
        sql.session.add(notification)
        sql.session.commit()

    @classmethod
    def get(cls, notificationId):
        notification: Notification = sql.session.query(Notification).filter(
            Notification.notification_id == notificationId).first()
        return notification

    @classmethod
    def markAsSeen(cls, notificationId):
        notification: Notification = cls.get(notificationId)
        notification.seen = True
        sql.session.commit()

    @classmethod
    def getAll(cls, userId):
        notifications: list[Notification] = sql.session.query(Notification).filter(Notification.receiver_id == userId).all()
        return notifications
