class Vehicle:

    def __init__(self, vehicle_make, vehicle_model, vehicle_regno):
        self.vehicle_make = vehicle_make
        self.vehicle_model = vehicle_model
        self.vehicle_regno = vehicle_regno

    def vehicle_info(self):
        print(f"Vehicle make : {self.vehicle_make}\nVehicle model : {self.vehicle_model}\nVehicle Regno : {self.vehicle_regno}")

class Employee:

    def __init__(self, emp_name, vehicle):
            self.emp_name = emp_name
            self.vehicle = vehicle

    def vehicle_info(self):
        print(f"{self.emp_name} vehicle informations are :")
        self.vehicle.vehicle_info()

vehicle = Vehicle('Toyota', '1998', 'AXR CTR')
emp_one = Employee("John", vehicle)
emp_one.vehicle_info()
