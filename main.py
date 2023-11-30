from vehicle import Vehicle
from vehicle_pass import Pass
from collections import Counter
from datetime import datetime

class TrafficSystem:
    """A data structure for storing the current state of the traffic system.

    Attributes:
        vehicle_register (dict): Dictionary of all vehicles with corresponding registration
        numbers as keys.

        passes (list): List of all recorded vehicle passes.
    
    Methods:
        
    """
    def __init__(self, data_path: str) -> None:
        """Initializes object with the given attributes.

        Args:
            data_path (str): The path of the .txt file to be read.
        """
        data = read_data(data_path)
        self.vehicle_register = data[0]
        self.passes = data[1]
        pass

    def most_active_hour(self):
        """Finds the date where most passes occured, and the hour of this date in which the most passes occured.
        
        Returns:
            hour (datetime): The most common pass date and hour.
    

        """
        most_common_date = Counter([x.date for x in self.passes]).most_common()[0][0]
        most_common_hour = Counter([x.time for x in self.passes if x.date == most_common_date]).most_common()[0][0]
        if len(most_common_hour) < 2:
            most_common_hour = "0" + most_common_hour

        time = datetime.strptime(most_common_date + most_common_hour, "%Y%m%d%H")
        
        return time

    def most_active_vehicle(self):
        most_common_reg_number = Counter([x.registration_number for x in self.passes]).most_common()[0][0]
        return self.vehicle_register[most_common_reg_number]
        
def read_data(file_path: str):
    """Reads vehicle- and pass data from a .txt file.

    Args:
        file_path (str): The location of the file. 

    Returns:
        vehicle_register (dict): Register of all vehicles with corresponding registration numbers
        as keys.

        passes (list): Register of all passes.
    """
    vehicle_register = {}
    passes = []
    data = open(file_path, 'r')
    lines = data.readlines()

    #linje 1 med passering
    pass_data = lines[0].split(';')
    for entry in pass_data:
        data = entry.split(",")
        if len(data) < 3:
            continue
        #dato, tid, reg. nummer
        new_pass = Pass(str(data[0]), str(data[1]), str(data[2]))
        passes.append(new_pass)

    #linje 2 med kjøretøyregister
    vehicle_data = lines[1].split(';')
    for entry in vehicle_data:  
        data = entry.split(",")
        if len(data) < 5:
            continue

        brand_and_model = data[1].split(" ")
        brand = brand_and_model[0]
        model = brand_and_model[1]
        new_vehicle = Vehicle(brand, str(data[4]), model, str(data[2]))
        vehicle_register[data[0]] = new_vehicle

    return (vehicle_register, passes)

#initialiserer trafikksystemet
system = TrafficSystem('input.txt')

most_active_hour = system.most_active_hour()
vehicle = system.most_active_vehicle()

#formaterer dato og time
date = most_active_hour.strftime('%Y-%m-%d')
hour = most_active_hour.strftime('%H')
print(f"Datoen med flest passeringer var {date}, og timen på den datoen med flest passeringer var time {hour}. \nKjøretøyet som passerte flest ganger var en {vehicle.brand} {vehicle.model} ({vehicle.category}) eid av {vehicle.owner}.")