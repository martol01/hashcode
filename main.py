def main():
    print('Hello World')



class Ride():
    def __init__( self, rideId, startTuple, finishTuple ):
        self.rideId = rideId
        self.startTuple = startTuple
        self.finishTuple = finishTuple
        self.isDone = False
        self.isAssigned = False

    def setIsAssigned(self , isAssigned ):
        self.isAssigned = isAssigned

    def isDone(self , isDone ):
        self.isDone  = isDone


class Vehicle():
    def __init__(self):
        pass


class DrivingManager():
    pass