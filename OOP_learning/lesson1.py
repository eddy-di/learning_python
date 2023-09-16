# Class Constructor/Initializer (__init__ & self)

class Car:
    # Class Attributes/Variables 
    tires_num = 4
    steering_wheel_num = 1
    transmission = 'manual' # or 'automatic'

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self):
        #Object Attributes/Variables
        self.make = 'Ford'
        self.model = 'Mustang'
        self.year = 2010
        self.color = 'Green'
        self.moon_roof = True
        self.engine_running = False
    
    # Methods

    def start_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = True 
    
    def stop_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = False