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
    if len(data) < 3:
        continue
    #dato, tid, reg. nummer
    newPass = Pass(int(data[0]), int(data[1]), str(data[2]))
    passes.append(newPass)

#linje 2 med kjøretøyregister
vehicleData = lines[1].split(';')
for entry in vehicleData:  
    data = entry.split(",")
    if len(data) < 5:
        continue
    #reg. nummer, 
    brandModel = data[1].split(" ")
    brand = brandModel[0]
    model = brandModel[1]
    newVehicle = Vehicle(brand, str(data[4]), model, str(data[2]))
    vehicleRegister[data[0]] = newVehicle

for pass1 in passes:
    print(pass1.registration_number)

print(vehicleRegister.keys())

def getVehicleRegister():
    pass

def getPasses():
    pass

def mostActiveVehicle():
    pass

def mostActiveDate():
    pass