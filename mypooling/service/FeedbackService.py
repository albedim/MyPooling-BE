from flask import jsonify
from mypooling.model.entity.Feedback import Feedback
from mypooling.model.entity.User import User
from mypooling.model.repository.FeedBackRepository import FeedbackRepository
from mypooling.service.UserService import UserService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/02/23
# Created at: 00:14
# Version: 1.0.0
# Description: This is the class for the feedback service
#


class FeedbackService():

    @classmethod
    def addFeedback(cls, request: dict):
        try:
            FeedbackRepository.addFeedback(
                request['creator_id'],
                request['receiver_id'],
                request['anonymous'],
                request['stars'],
                request['thought']
            )
            return Utils.createSuccessResponse(True, Constants.CREATED), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 400), 400

    @classmethod
    def getFeedbacks(cls, userId):
        try:
            feedbacks: list[Feedback] = FeedbackRepository.getFeedbacks(userId)
            result: list[dict] = []
            for feedback in feedbacks:
                if feedback.anonymous:
                    result.append(feedback.toJson_Anonymous())
                else:
                    creator: dict = UserService.getUser(feedback.creator_id)
                    result.append(feedback.toJson_Not_Anonymous(creator))
            return jsonify(result), 200
        except KeyError:
            return Utils.createWrongResponse(False, Constants.INVALID_REQUEST, 405)

    @classmethod
    def getAverageStars(cls, feedBacks) -> float:
        if len(feedBacks) == 0:
            return 0
        sumAverage = 0
        for feedBack in feedBacks:
            sumAverage += feedBack.stars
        return sumAverage / len(feedBacks)