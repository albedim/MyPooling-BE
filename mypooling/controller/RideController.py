from flasgger import swag_from
from flask import Blueprint, request
from flask_cors import cross_origin

from mypooling.service.RideService import RideService
from mypooling.utils.Utils import Utils


ride: Blueprint = Blueprint('RideController', __name__, url_prefix=Utils.getURL('ride'))


@ride.route("/add", methods=['POST'])
@cross_origin()
@swag_from('./docs/ride/add.yaml')
def add():
    return RideService.addRide(request.json)


@ride.route("/get/<tripId>", methods=['GET'])
@cross_origin()
@swag_from('./docs/ride/get.yaml')
def get(tripId: int):
    return RideService.getRiders(tripId)




