from mypooling.configuration.config import sql

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user entity
#


class User(sql.Model):
    __tablename__ = 'users'
    user_id: int = sql.Column(sql.Integer, primary_key=True)
    name: str = sql.Column(sql.String(20), nullable=False)
    email: str = sql.Column(sql.String(40), nullable=False)
    password: str = sql.Column(sql.String(40), nullable=False)
    birthday: int = sql.Column(sql.Date, nullable=False)
    place: str = sql.Column(sql.String(40), nullable=False)
    bio: str = sql.Column(sql.String(150), nullable=True)
    password_forgotten_token: str = sql.Column(sql.String(540), nullable=True)
    username: str = sql.Column(sql.String(40), nullable=False)

    def __init__(self, username, name, email, age, bio, place, password):
        self.name = name
        self.username = username
        self.email = email
        self.age = age,
        self.bio = bio,
        self.place = place,
        self.password_forgotten_token = None
        self.password = password

    def toJson(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'age': self.age,
            'bio': self.bio,
            'place': self.place,
            'username': self.username,
        }

    def toJson_Information(self, feedbacksNumber, ownTripsNumber, ridingTripsNumber, averageStars):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'username': self.username,
            'more_information': {
                'feedbacks': feedbacksNumber,
                'own_trips': ownTripsNumber,
                'riding_trips': ridingTripsNumber
            },
            'age': self.age,
            'bio': self.bio,
            'place': self.place,
            'average_stars': averageStars
        }
