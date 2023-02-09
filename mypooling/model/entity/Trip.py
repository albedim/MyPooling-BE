import datetime

from sqlalchemy.orm import relationship

from mypooling.configuration.config import sql
from mypooling.model.entity.Step import Step
from mypooling.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 17:34
# Version: 1.0.0
# Description: This is the class for the trip entity
#


class Trip(sql.Model):
    __tablename__ = 'trips'
    trip_id: int = sql.Column(sql.Integer, primary_key=True)
    departure_date: str = sql.Column(sql.DateTime, nullable=False)
    creation_date: str = sql.Column(sql.DateTime, nullable=False)
    start_x: float = sql.Column(sql.Float, nullable=False)
    start_y: float = sql.Column(sql.Float, nullable=False)
    owner_id: int = sql.Column(sql.Integer, nullable=False)
    finished: bool = sql.Column(sql.Boolean, nullable=False)
    slots: int = sql.Column(sql.Integer, nullable=False)
    code: str = sql.Column(sql.String(6), nullable=False)
    used_slots: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, departure_date, start_x, start_y, owner_id, slots):
        self.departure_date = departure_date
        self.start_x = start_x
        self.start_y = start_y
        self.owner_id = owner_id
        self.slots = slots
        self.used_slots = 0
        self.code = Utils.createLink(6).upper()
        self.finished = False
        self.creation_date = str(datetime.datetime.now())

    def toJson(self):
        return {
            'trip_id': self.trip_id,
            'departure_date': str(self.departure_date),
            'creation_date': str(self.creation_date),
            'start_x': self.start_x,
            'start_y': self.start_y,
            'owner_id': self.owner_id,
            'finished': self.finished,
            'slots': self.slots,
            'code': self.code,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots
        }

    def toJson_Step_Owner(self, owner: dict, step: dict):
        return {
            'trip_id': self.trip_id,
            'departure_date': str(self.departure_date),
            'creation_date': str(self.creation_date),
            'start_x': self.start_x,
            'start_y': self.start_y,
            'owner_id': self.owner_id,
            'finished': self.finished,
            'slots': self.slots,
            'code': self.code,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'step': step,
            'owner': owner
        }

    def toJson_Owner(self, owner: dict):
        return {
            'trip_id': self.trip_id,
            'departure_date': str(self.departure_date),
            'creation_date': str(self.creation_date),
            'start_x': self.start_x,
            'start_y': self.start_y,
            'owner_id': self.owner_id,
            'finished': self.finished,
            'slots': self.slots,
            'code': self.code,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'owner': owner
        }

    def toJson_Steps(self, steps: list[dict]):
        return {
            'trip_id': self.trip_id,
            'departure_date': str(self.departure_date),
            'creation_date': str(self.creation_date),
            'start_x': self.start_x,
            'start_y': self.start_y,
            'owner_id': self.owner_id,
            'finished': self.finished,
            'slots': self.slots,
            'code': self.code,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'steps': steps
        }
