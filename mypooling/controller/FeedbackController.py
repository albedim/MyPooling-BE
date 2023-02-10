from flasgger import swag_from
from flask import Blueprint, request
from flask_cors import cross_origin

from mypooling.service.FeedbackService import FeedbackService
from mypooling.utils.Utils import Utils


feedback: Blueprint = Blueprint('FeedbackController', __name__, url_prefix=Utils.getURL('feedback'))


@feedback.route("/add", methods=['POST'])
@cross_origin()
@swag_from('./docs/feedback/add.yaml')
def add():
    return FeedbackService.addFeedback(request.json)


@feedback.route("/get", methods=['GET'])
@cross_origin()
@swag_from('./docs/feedback/get.yaml')
def get():
    return FeedbackService.getFeedbacks(int(request.args.get('user_id')), request.args.get('anonymous'))




