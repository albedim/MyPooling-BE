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
    date: str = sql.Column(sql.DateTime, nullable=False)
    creation_date: str = sql.Column(sql.DateTime, nullable=False)
    owner_id: int = sql.Column(sql.Integer, nullable=False)
    slots: int = sql.Column(sql.Integer, nullable=False)
    code: str = sql.Column(sql.String(6), nullable=False)
    mode: str = sql.Column(sql.String(10), nullable=False)
    used_slots: int = sql.Column(sql.Integer, nullable=False)

    def __init__(self, date, owner_id, slots, mode):
        self.date = date
        self.owner_id = owner_id
        self.slots = slots
        self.used_slots = 0
        self.mode = mode
        self.code = Utils.createLink(6).upper()
        self.creation_date = str(datetime.datetime.now())

    def toJson(self):
        return {
            'trip_id': self.trip_id,
            'date': str(self.date),
            'creation_date': str(self.creation_date),
            'owner_id': self.owner_id,
            'slots': self.slots,
            'code': self.code,
            'mode': self.mode,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots
        }

    def toJson_Steps_Owner(self, owner: dict, steps: list):
        return {
            'trip_id': self.trip_id,
            'date': str(self.date),
            'creation_date': str(self.creation_date),
            'owner_id': self.owner_id,
            'slots': self.slots,
            'code': self.code,
            'mode': self.mode,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'steps': steps,
            'owner': owner
        }

    def toJson_Step_Owner(self, owner: dict, step: dict):
        return {
            'trip_id': self.trip_id,
            'date': str(self.date),
            'creation_date': str(self.creation_date),
            'owner_id': self.owner_id,
            'slots': self.slots,
            'code': self.code,
            'mode': self.mode,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'step': step,
            'owner': owner
        }

    def toJson_Owner(self, owner: dict):
        return {
            'trip_id': self.trip_id,
            'date': str(self.date),
            'creation_date': str(self.creation_date),
            'owner_id': self.owner_id,
            'slots': self.slots,
            'code': self.code,
            'mode': self.mode,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'owner': owner
        }

    def toJson_Steps(self, steps: list[dict]):
        return {
            'trip_id': self.trip_id,
            'date': str(self.date),
            'creation_date': str(self.creation_date),
            'owner_id': self.owner_id,
            'slots': self.slots,
            'code': self.code,
            'mode': self.mode,
            'used_slots': self.used_slots,
            'available': self.used_slots < self.slots,
            'steps': steps
        }
