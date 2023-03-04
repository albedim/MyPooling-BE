from sqlalchemy import asc, desc

from mypooling.configuration.config import sql
from mypooling.model.entity.Feedback import Feedback

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/02/23
# Created at: 00:14
# Version: 1.0.0
# Description: This is the class for the feedback repository
#


class FeedbackRepository():

    @classmethod
    def addFeedback(cls, creator_id, receiver_id, anonymous, stars, thought):
        feedback: Feedback = Feedback(anonymous, creator_id, receiver_id, stars, thought)
        sql.session.add(feedback)
        sql.session.commit()

    @classmethod
    def getFeedbacks(cls, userId):
        feedbacks: list[Feedback] = sql.session.query(Feedback).filter(Feedback.receiver_id == userId).order_by(desc(Feedback.feedback_id)).all()
        return feedbacks


