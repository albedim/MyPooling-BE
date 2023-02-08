from mypooling.configuration.config import sql
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.Step import Step
from mypooling.model.entity.User import User


class StepRepository():

    @classmethod
    def getStepByName(cls, stepName, tripId) -> Step:
        step: Step = sql.session.query(Step).filter(Step.trip_id == tripId).filter(Step.name == stepName).first()
        return step

    @classmethod
    def getStep(cls, stepId) -> Ride:
        ride: Ride = sql.session.query(Step).filter(Step.step_id == stepId).first()
        return ride

    @classmethod
    def addStep(cls, name, x, y, tripId):
        step: Step = Step(name, x, y, tripId)
        sql.session.add(step)
        sql.session.commit()

    @classmethod
    def getSteps(cls, tripId) -> list:
        steps: list[Step] = sql.session.query(Step).filter(Step.trip_id == tripId).all()
        return steps
