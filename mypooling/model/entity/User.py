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
    username: str = sql.Column(sql.String(40), nullable=False)

    def __init__(self, username, name, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = password

    def toJson(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'username': self.username,
        }
