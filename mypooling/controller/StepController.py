from flasgger import swag_from
from flask import Blueprint, request
from flask_cors import cross_origin
from mypooling.service.StepService import StepService
from mypooling.utils.Utils import Utils


step: Blueprint = Blueprint('StepController', __name__, url_prefix=Utils.getURL('step'))


@step.route("/add/<tripId>", methods=['POST'])
@cross_origin()
@swag_from('./docs/step/add.yaml')
def add(tripId: int):
    return StepService.addStep(tripId, request.json)




