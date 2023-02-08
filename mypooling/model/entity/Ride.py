from mypooling.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 18:34
# Version: 1.0.0
# Description: This is the class for the ride entity
#


class Ride(sql.Model):
    __tablename__ = 'rides'
    ride_id: int = sql.Column(sql.Integer, primary_key=True)
    user_id: int = sql.Column(sql.Integer, nullable=False)
    trip_id: int = sql.Column(sql.Integer, nullable=False)
    step_id: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, user_id, step_id, trip_id):
        self.user_id = user_id
        self.step_id = step_id
        self.trip_id = trip_id

    def toJson(self):
        return {
            'ride_id': self.ride_id,
            'user_id': self.user_id,
            'trip_id': self.trip_id,
            'step_id': self.step_id
        }

    def toJson_User(self, user: dict):
        return {
            'ride_id': self.ride_id,
            'user_id': self.user_id,
            'trip_id': self.trip_id,
            'step_id': self.step_id,
            'user': user
        }
