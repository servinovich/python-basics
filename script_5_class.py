# script_5_class.py

class Vehicle:
    color = "white"
    
    # Constructor
    def __init__(self, model, speed, mileage):
        self.model = model
        self.speed = speed 
        self.mileage = mileage
        self.capacity = None

    def seats (self, capacity):
        self.capacity = capacity

    def display(self):
        print ("\nProperties of Vehicle: ")
        print ("Model: ", self.model)
        print ("Color: ", self.color)
        print ("Max speed: ", self.speed)
        print ("Miles: ", self.mileage) 
        print ("Capacity: ", self.capacity) 
        
# Creating objects of the Vehicle class
veh1 = Vehicle('Honda', 250, 20)
veh1.seats (4)
veh1.display()

veh2 = Vehicle('Lexus', 350, 50)
veh2.seats (2)
veh2.display()