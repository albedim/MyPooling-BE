from mypooling.configuration.config import sql
from mypooling.model.entity.Feedback import Feedback
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.User import User


class FeedbackRepository():

    @classmethod
    def addFeedback(cls, creator_id, receiver_id, stars, thought):
        feedback: Feedback = Feedback(creator_id, receiver_id, stars, thought)
        sql.session.add(feedback)
        sql.session.commit()

    @classmethod
    def getFeedbacks(cls, userId):
        feedbacks: list[Feedback] = sql.session.query(Feedback).filter(Feedback.receiver_id == userId).all()
        return feedbacks


