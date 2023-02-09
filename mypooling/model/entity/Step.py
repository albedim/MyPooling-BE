from mypooling.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 16:14
# Version: 1.0.0
# Description: This is the class for the step entity
#


class Step(sql.Model):
    __tablename__ = 'steps'
    step_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(40), nullable=False)
    x: float = sql.Column(sql.Double, nullable=False)
    y: float = sql.Column(sql.Double, nullable=False)
    place_id: int = sql.Column(sql.Integer, nullable=False)
    trip_id: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, place_id, name, x, y, trip_id):
        self.name = name
        self.x = x
        self.y = y
        self.place_id = place_id
        self.trip_id = trip_id

    def toJson(self):
        return {
            'step_id': self.step_id,
            'x': self.x,
            'y': self.y,
            'place_id': self.place_id,
            'trip_id': self.trip_id
        }
