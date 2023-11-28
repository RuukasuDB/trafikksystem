from vehicle import Vehicle
from vehicle_pass import Pass
import pandas as pd

vehicleRegister = {}
passes = []

data = open('input.txt', 'r')
lines = data.readlines()

#linje 1 med passering
passData = lines[0].split(';')
for entry in passData:
    
    data = entry.split(",")
    if len(data < 3):
        continue
    #dato, tid, reg. nummer
    newPass = Pass(int(data[0]), int(data[1]), str(data[2]))

#linje 2 med kjøretøyregister
vehicleData = lines[1].split(';')
for entry in vehicleData:  
    data = entry.split(",")
    if len(data < 5):
        continue
    #dato, tid, reg. nummer
    newVehicle = Vehicle(str(data[1]), int(data[1]), str(data[2]))


def getVehicleRegister():
    pass

def getPasses():
    pass

def mostActiveVehicle():
    pass

def mostActiveDate():
    pass