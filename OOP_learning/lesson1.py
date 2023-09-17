# Class Constructor/Initializer (__init__ & self)

class Car:
    # Class Attributes/Variables 
    tires_num = 4
    steering_wheel_num = 1
    transmission = 'manual' # or 'automatic'

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, make, model, year, color, moon_roof=False):
        # Object Attributes/Variables previous values were hard coded to class and it was not aplicable for universal use
        # To make it universal the parameters named like below have to be added after self in brackets above
        self.make = make # this kind of attributes setting in class is preferable.
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False
    
    # Methods

    def start_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = True 
    
    def stop_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = False