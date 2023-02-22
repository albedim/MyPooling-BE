from mypooling.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 09/02/23
# Created at: 00:14
# Version: 1.0.0
# Description: This is the class for the feedback entity
#


class Feedback(sql.Model):
    __tablename__ = 'feedbacks'
    feedback_id: int = sql.Column(sql.Integer, primary_key=True)
    creator_id: int = sql.Column(sql.Integer, nullable=True)
    receiver_id: int = sql.Column(sql.Integer, nullable=False)
    stars: int = sql.Column(sql.Integer, nullable=False)
    anonymous: bool = sql.Column(sql.Boolean, nullable=False)
    thought: str = sql.Column(sql.String(240), nullable=True)

    def __init__(self, anonymous, creator_id, receiver_id, stars, thought):
        self.creator_id = creator_id
        self.receiver_id = receiver_id
        self.stars = stars
        self.anonymous = anonymous
        self.thought = thought

    def toJson(self):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'anonymous': self.anonymous,
            'stars': self.stars,
            'thought': self.thought
        }

    def toJson_Not_Anonymous(self, creator: dict):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'stars': self.stars,
            'thought': self.thought,
            'anonymous': self.anonymous,
            'creator': creator
        }

    def toJson_Anonymous(self):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'stars': self.stars,
            'anonymous': self.anonymous,
            'thought': self.thought,
            'creator': 'Anonymous'
        }
