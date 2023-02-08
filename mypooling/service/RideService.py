from mypooling.model.entity.Ride import Ride
from mypooling.model.repository.RideRepositroy import RideRepository
from mypooling.service.trips.SlotsService import SlotsService
from mypooling.service.UserService import UserService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 18:34
# Version: 1.0.0
# Description: This is the class for the ride service
#


class RideService():

    @classmethod
    def addRide(cls, request: dict):
        try:
            if cls.isRider(request['user_id'], request['trip_id']):
                return Utils.createWrongResponse(False, Constants.ALREADY_CREATED, 403)
            if not SlotsService.hasSlots(request['trip_id']):
                return Utils.createWrongResponse(False, Constants.FULL_SLOTS, 403)
            RideRepository.addRide(request['user_id'], request['step_id'], request['trip_id'])
            return Utils.createSuccessResponse(True, Constants.CREATED)
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getRiders(cls, tripId: int):
        try:
            rides: list[Ride] = RideRepository.getRides(tripId)
            result: list[dict] = []
            for ride in rides:
                user: dict = UserService.getUser(ride.user_id)
                result.append(ride.toJson_User(user))
            return result
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def isRider(cls, userId, tripId) -> bool:
        return RideRepository.getRide(userId, tripId) is not None

    @classmethod
    def getRide(cls, userId, tripId):
        return RideRepository.getRide(userId, tripId)