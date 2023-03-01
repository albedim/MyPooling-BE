from mypooling.model.entity.User import User
from mypooling.model.repository.FeedBackRepository import FeedbackRepository
from mypooling.model.repository.TripRepository import TripRepository
from mypooling.model.repository.UserRepository import UserRepository
from mypooling.service.FeedbackService import FeedbackService
from mypooling.utils.Constants import Constants
from mypooling.utils.Utils import Utils

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 21/02/23
# Created at: 14:34
# Version: 1.0.0
# Description: This is the class for the user information service
#


class UserInformationService():

    @classmethod
    def getUserInformation(cls, userId, username):
        try:
            user: User = UserRepository.getUserById(userId) \
                if userId is not None else UserRepository.getUserByUsername(username)
            return user.toJson_Information(
                len(FeedbackRepository.getFeedbacks(user.user_id)),
                len(TripRepository.getOwnTrips(user.user_id)),
                len(TripRepository.getRidingTrips(user.user_id)),
                FeedbackService.getAverageStars(user.user_id)
            )
        except AttributeError:
            return Utils.createWrongResponse(False, Constants.NOT_FOUND, 404), 404