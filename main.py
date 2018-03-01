import os

EXAMPLE_1 = 'a_example.in'

def main():
    pwd = os.path.dirname(os.path.realpath(_file_))
    file = '{}\\{}'.format( pwd, EXAMPLE_1)
    lst = list(open(file))

    rows, columns, vehicles, rides, bonus, total = lst[ 0 ].split( )

    manager = DrivingManager( rows, columns, vehicles, rides, bonus, total )



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


class Vehicle( ):
    def __init__(self, vehicleId ):
        self.vehicleId = vehicleId


class DrivingManager():

    def __init__(self, numRows, numColumns, numVehicles, numRides, rideBonus, totalSteps):
        self.numRows = numRows
        self.numColumns = numColumns
        self.numVehicles = numVehicles
        self.numRides = numRides
        self.rideBonus = rideBonus
        self.totalSteps = totalSteps
        self.rides = []
        self.vehicles = []

    def getRemainingSteps(self ):
        return self.totalSteps

    def reduceRemainingSteps(self, numSteps=1):
        self.totalSteps -= numSteps

    def createVehicle(self):
        vehicle = Vehicle()
        self.vehicles.append( vehicle )

    def createRide(self, rideId, startTuple, finishTuple  ):
        ride = Ride( rideId, startTuple, finishTuple )
        self.rides.append( ride )

    def getRide(self, rideId ):
        for rideObj in self.rides:
            if rideObj.rideId == rideId:
                return rideObj

    def getVehicle(self, vehicleId):
        for vehicleObj in self.vehicles:
            if vehicleObj.rideId == vehicleId:
                return vehicleObj
