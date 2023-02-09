from flask import Blueprint, request
from flask_cors import cross_origin
from mypooling.service.trips.TripService import TripService
from mypooling.utils.Utils import Utils


trip: Blueprint = Blueprint('TripController', __name__, url_prefix=Utils.getURL('trip'))


@trip.route("/add", methods=['POST'])
@cross_origin()
def add():
    return TripService.addTrip(request.json)


@trip.route("/get/near", methods=['GET'])
@cross_origin()
def getNear():
    return TripService.getNearTrips(request.json)


@trip.route("/get/riding/<userId>", methods=['GET'])
@cross_origin()
def getRiding(userId: int):
    return TripService.getRidingTrips(userId)


@trip.route("/get/own/<ownerId>", methods=['GET'])
@cross_origin()
def getOwn(ownerId: int):
    return TripService.getOwnTrips(ownerId)




