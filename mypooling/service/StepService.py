from mypooling.model.repository.StepRepositroy import StepRepository
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 16:14
# Version: 1.0.0
# Description: This is the class for the step service
#


class StepService():

    @classmethod
    def addStep(cls, tripId: int, request: dict):
        try:
            for o in request:
                StepRepository.addStep(o['place_id'], o['details'], o['time'], o['name'], o['x'], o['y'], tripId)
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def getSteps(cls, tripId: int):
        try:
            return StepRepository.getSteps(tripId)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getStepById(cls, tripId, placeId: int):
        try:
            return StepRepository.getStepById(placeId, tripId).toJson()
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getStep(cls, stepId):
        return StepRepository.getStep(stepId).toJson()