from mypooling.configuration.config import sql
from mypooling.model.entity.User import User
from mypooling.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the user repository
#

class UserRepository():

    @classmethod
    def signin(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, username, name, email, age, bio, place, password) -> None:
        user: User = User(username, name, email, age, bio, place, password)
        sql.session.add(user)
        sql.session.commit()

    @classmethod
    def existsByEmail(cls, email):
        users: User = sql.session.query(User).filter(User.email == email).count()
        return users

    @classmethod
    def existsByUsername(cls, username):
        users: User = sql.session.query(User).filter(User.username == username).count()
        return users

    @classmethod
    def getUserById(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user

    @classmethod
    def getUserByUsername(cls, username) -> User:
        user: User = sql.session.query(User).filter(User.username == username).first()
        return user

    @classmethod
    def getUserByEmail(cls, email) -> User:
        user: User = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def createForgottenPasswordToken(cls, user, token):
        user.password_forgotten_token = token
        sql.session.commit()

    @classmethod
    def getUserByPasswordForgottenToken(cls, token):
        user: User = sql.session.query(User).filter(User.password_forgotten_token == token).first()
        return user

    @classmethod
    def changePassword(cls, userId, newPassword):
        user: User = cls.getUserById(userId)
        user.password = newPassword
        sql.session.commit()

    @classmethod
    def changeData(cls, userId, username, name, email, age, bio, place, password) -> None:
        user: User = cls.getUserById(userId)
        user.username = username
        user.name = name
        user.email = email
        user.age = age
        user.place = place
        user.password = password
        user.bio = bio
        sql.session.commit()
