from mypooling.configuration.config import sql


class Feedback(sql.Model):
    __tablename__ = 'feedbacks'
    feedback_id: int = sql.Column(sql.Integer, primary_key=True)
    creator_id: int = sql.Column(sql.Integer, nullable=True)
    receiver_id: int = sql.Column(sql.Integer, nullable=False)
    stars: int = sql.Column(sql.Integer, nullable=False)
    thought: str = sql.Column(sql.String(240), nullable=True)

    def __init__(self, creator_id, receiver_id, stars, thought):
        self.creator_id = creator_id
        self.receiver_id = receiver_id
        self.stars = stars
        self.thought = thought

    def toJson(self):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'stars': self.stars,
            'thought': self.thought
        }

    def toJson_Creator_Receiver(self, creator: dict, receiver: dict):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'stars': self.stars,
            'thought': self.thought,
            'creator': creator,
            'receiver': receiver
        }

    def toJson_Receiver(self, receiver: dict):
        return {
            'feedback_id': self.feedback_id,
            'creator_id': self.creator_id,
            'receiver_id': self.receiver_id,
            'stars': self.stars,
            'thought': self.thought,
            'creator': 'Anonymous',
            'receiver': receiver
        }
