from mypooling.configuration.config import sql
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.Step import Step

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 16:14
# Version: 1.0.0
# Description: This is the class for the step repository
#


class StepRepository():

    @classmethod
    def getStepById(cls, placeId, tripId) -> Step:
        step: Step = sql.session.query(Step).filter(Step.trip_id == tripId).filter(Step.place_id == placeId).first()
        return step

    @classmethod
    def getStep(cls, stepId) -> Ride:
        ride: Ride = sql.session.query(Step).filter(Step.step_id == stepId).first()
        return ride

    @classmethod
    def addStep(cls, placeId, time, name, x, y, tripId):
        step: Step = Step(placeId, time, name, x, y, tripId)
        sql.session.add(step)
        sql.session.commit()

    @classmethod
    def getSteps(cls, tripId) -> list:
        steps: list[Step] = sql.session.query(Step).filter(Step.trip_id == tripId).all()
        return steps
