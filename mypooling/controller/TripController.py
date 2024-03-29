from flasgger import swag_from
from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required

from mypooling.service.trips.TripService import TripService
from mypooling.utils.Utils import Utils


trip: Blueprint = Blueprint('TripController', __name__, url_prefix=Utils.getURL('trip'))


@trip.route("/add", methods=['POST'])
@cross_origin()
@swag_from('./docs/trip/add.yaml')
def add():
    return TripService.addTrip(request.json)


@trip.route("/get/near", methods=['GET'])
@cross_origin()
@jwt_required()
@swag_from('./docs/trip/get_near.yaml')
def getNear():
    return TripService.getNearTrips(
        get_jwt_identity()['user_id'],
        float(request.args.get('x')),
        float(request.args.get('y')),
        int(request.args.get('strength')),
        request.args.get('date'),
        request.args.get('mode')
    )


@trip.route("/get/riding/<userId>", methods=['GET'])
@cross_origin()
@swag_from('./docs/trip/get_riding.yaml')
def getRiding(userId: int):
    return TripService.getRidingTrips(userId)


@trip.route("/get/own/<ownerId>", methods=['GET'])
@cross_origin()
@swag_from('./docs/trip/get_own.yaml')
def getOwn(ownerId: int):
    return TripService.getOwnTrips(ownerId)




