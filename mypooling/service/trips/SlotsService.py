from mypooling.model.repository.TripRepository import TripRepository

#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 17:34
# Version: 1.0.0
# Description: This is the class for the slots service
#

class SlotsService():

    @classmethod
    def addSlot(cls, tripId) -> bool:
        return TripRepository.addSlot(tripId)

    @classmethod
    def hasSlots(cls, tripId):
        return TripRepository.hasSlots(tripId) > 0