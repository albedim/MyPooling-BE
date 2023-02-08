from mypooling.model.repository.StepRepositroy import StepRepository
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils


class StepService():

    @classmethod
    def addStep(cls, tripId: int, request: dict):
        try:
            for o in request:
                StepRepository.addStep(o['name'], o['x'], o['y'], tripId)
            return Utils.createSuccessResponse(True, "")
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getSteps(cls, tripId: int):
        try:
            return StepRepository.getSteps(tripId)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getStepByName(cls, tripId, stepName: str):
        try:
            return StepRepository.getStepByName(stepName, tripId).toJson()
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getStep(cls, stepId):
        return StepRepository.getStep(stepId).toJson()