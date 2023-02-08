from mypooling.configuration.config import sql
from mypooling.model.entity.Ride import Ride
from mypooling.model.entity.User import User


class RideRepository():

    @classmethod
    def getRides(cls, tripId) -> list[Ride]:
        rides: list[Ride] = sql.session.query(Ride).filter(Ride.trip_id == tripId).all()
        return rides

    @classmethod
    def getRide(cls, userId, tripId) -> Ride:
        ride: Ride = sql.session.query(Ride).filter(Ride.trip_id == tripId).filter(Ride.user_id == userId).first()
        return ride

    @classmethod
    def exists(cls, email):
        users: User = sql.session.query(User).filter(User.email == email).count()
        return users

    @classmethod
    def getUser(cls, userId) -> User:
        user: User = sql.session.query(User).filter(User.userId == userId).first()
        return user

    @classmethod
    def addRide(cls, userId, stepId, tripId):
        step: Ride = Ride(userId, stepId, tripId)
        sql.session.add(step)
        sql.session.commit()
