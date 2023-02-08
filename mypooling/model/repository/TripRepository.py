from sqlalchemy import text, desc
from mypooling.configuration.config import sql
from mypooling.model.entity.Trip import Trip

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 17:34
# Version: 1.0.0
# Description: This is the class for the trip repository
#


class TripRepository():

    @classmethod
    def getOwnTrips(cls, ownerId) -> list[Trip]:
        trips: list[Trip] = sql.session.query(Trip).filter(Trip.owner_id == ownerId).all()
        return trips

    @classmethod
    def addSlot(cls, tripId):
        trip: Trip = sql.session.query(Trip).filter(Trip.trip_id == tripId).first()
        trip.used_slots += 1
        sql.session.commit()

    @classmethod
    def hasSlots(cls, tripId):
        trips: int = sql.session.query(Trip).filter(Trip.trip_id == tripId).filter(Trip.used_slots < Trip.slots).count()
        return trips

    @classmethod
    def getNearTrips(cls, stepName) -> list:
        trips: list[Trip] = sql.session.query(Trip).from_statement(
            text("SELECT trips.* "
                 "FROM trips "
                 "JOIN steps "
                 "ON trips.trip_id = steps.trip_id "
                 "WHERE steps.name = :stepName "
                 "AND trips.finished = false")
        ).params(stepName=stepName).all()
        return trips

    @classmethod
    def getRidingTrips(cls, userId):
        trips = sql.session.query(Trip).from_statement(
            text("SELECT trips.* "
                 "FROM trips "
                 "JOIN rides "
                 "ON trips.trip_id = rides.trip_id "
                 "WHERE rides.user_id = :userId "
                 "AND trips.finished = false")
        ).params(userId=userId).all()
        return trips

    @classmethod
    def getLastTripOf(cls, ownerId: int):
        lastTrip: Trip = sql.session.query(Trip).filter(Trip.owner_id == ownerId).order_by(desc(Trip.trip_id)).first()
        return lastTrip

    @classmethod
    def addTrip(cls, departure_date, start_x, start_y, owner_id, slots):
        trip: Trip = Trip(departure_date, start_x, start_y, owner_id, slots)
        sql.session.add(trip)
        sql.session.commit()