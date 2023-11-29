import datetime

from flask import jsonify
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.Step import Step
from mypooling.model.entity.Trip import Trip
from mypooling.model.repository.TripRepository import TripRepository
from mypooling.service.RideService import RideService
from mypooling.service.StepService import StepService
from mypooling.service.user.UserService import UserService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 17:34
# Version: 1.0.0
# Description: This is the class for the trip service
#


class TripService():

    @classmethod
    def addTrip(cls, request: dict):
        TripRepository.addTrip(
            datetime.datetime.fromisoformat(
                request['date'].split(',')[0] + '-' +
                request['date'].split(',')[1] + '-' +
                request['date'].split(',')[2] + ' ' +
                request['date'].split(',')[3] + ':' +
                request['date'].split(',')[4]
            ), request['owner_id'], request['slots'], request['mode']
        )
        return Utils.createSuccessResponse(True, TripRepository.getLastTripOf(request['owner_id']).trip_id), 200

    @classmethod
    def getOwnTrips(cls, ownerId: int):
        try:
            trips: list[Trip] = TripRepository.getOwnTrips(ownerId)
            result: list[dict] = []
            for trip in trips:
                steps: list[Step] = StepService.getSteps(trip.trip_id)
                result.append(trip.toJson_Steps(Utils.createList(steps)))
            return jsonify(result), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 200

    @classmethod
    def getNearTrips(cls, userId: int, x: float, y: float, strength: float, date: str, mode):
        try:
            # trips
            rows: list = TripRepository.getNearTrips(date.replace(",", "-", 2), x, y, strength, mode)
            result: list[dict] = []
            for row in rows:  # row has now two objects
                if row[0].owner_id != userId:
                    owner: dict = UserService.getUser(row[0].owner_id)  # trip owner
                    steps: list = StepService.getSteps(row[0].trip_id)  # trip's steps
                    finalSteps = []
                    for step in steps:
                        if step.step_id == row[1].step_id:  # if this step is the nearest one
                            finalSteps.append(step.toJson_Nearest(True))
                        else:
                            finalSteps.append(step.toJson_Nearest(False))
                    result.append(row[0].toJson_Steps_Owner(owner, cls.sortByNearest(finalSteps)))
                else:
                    return Utils.createWrongResponse(False, Constants.NOT_ENOUGH_PERMISSIONS, 306), 306
            return jsonify(result), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def getRidingTrips(cls, userId):
        try:
            trips: list[Trip] = TripRepository.getRidingTrips(userId)
            result: list[dict] = []
            for trip in trips:
                ride: Ride = RideService.getRide(userId, trip.trip_id)
                step: dict = StepService.getStep(ride.step_id)
                owner: dict = UserService.getUser(trip.owner_id)
                result.append(trip.toJson_Step_Owner(owner, step))
            return jsonify(result), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def sortByNearest(cls, steps):
        finalSteps = []
        nearestStep = None
        # append to finalSteps the nearest step
        for step in steps:
            if step['nearest']:
                finalSteps.append(step)
                nearestStep = step
        # append to finalSteps the steps which are not nearest
        for step in steps:
            if step != nearestStep:
                finalSteps.append(step)

        return finalSteps

