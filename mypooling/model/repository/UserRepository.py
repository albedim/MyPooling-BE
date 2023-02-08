from mypooling.configuration.config import sql
from mypooling.model.entity.User import User


class UserRepository():

    @classmethod
    def signin(cls, email, password) -> User:
        user: User = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def signup(cls, username, name, email, password) -> None:
        user: User = User(username, name, email, password)
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
    def getUser(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.user_id == userId).first()
        return user
