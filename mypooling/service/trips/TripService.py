import datetime

from flask import jsonify
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.Step import Step
from mypooling.model.entity.Trip import Trip
from mypooling.model.repository.TripRepository import TripRepository
from mypooling.service.RideService import RideService
from mypooling.service.StepService import StepService
from mypooling.service.UserService import UserService
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
        try:
            TripRepository.addTrip(
                datetime.datetime.fromisoformat(
                    request['departure_date'].split(',')[2] + '-' +
                    request['departure_date'].split(',')[1] + '-' +
                    request['departure_date'].split(',')[0] + ' ' +
                    request['departure_date'].split(',')[3] + ':' +
                    request['departure_date'].split(',')[4]
                ), request['start_x'], request['start_y'], request['owner_id'], request['slots']
            )
            return Utils.createSuccessResponse(True, TripRepository.getLastTripOf(request['owner_id']).trip_id)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getOwnTrips(cls, ownerId: int):
        try:
            trips: list[Trip] = TripRepository.getOwnTrips(ownerId)
            result: list[dict] = []
            for trip in trips:
                steps: list[Step] = StepService.getSteps(trip.trip_id)
                result.append(trip.toJson_Steps(Utils.createList(steps)))
            return jsonify(result)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 500)

    @classmethod
    def getNearTrips(cls, stepName: str):
        try:
            trips: list[Trip] = TripRepository.getNearTrips(stepName)
            result: list[dict] = []
            for trip in trips:
                step: dict = StepService.getStepByName(trip.trip_id, stepName)
                owner: dict = UserService.getUser(trip.owner_id)
                result.append(trip.toJson_Step_Owner(owner, step))
            return jsonify(result)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 500)

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
            return jsonify(result)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 500)