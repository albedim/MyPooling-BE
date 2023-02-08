from mypooling.model.repository.TripRepository import TripRepository


class SlotsService():

    @classmethod
    def addSlot(cls, tripId) -> bool:
        return TripRepository.addSlot(tripId)

    @classmethod
    def hasSlots(cls, tripId):
        return TripRepository.hasSlots(tripId) > 0