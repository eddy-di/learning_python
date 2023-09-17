# Class Constructor/Initializer (__init__ & self)

class Car:
    # Class Attributes/Variables 
    tires_num = 4
    steering_wheel_num = 1
    transmission = 'manual' # or 'automatic'

    # Class Constructor/Initializer (Method with a special name)
    def __init__(self):
        # Object Attributes/Variables previous values were hard coded to class and it was not aplicable for universal use
        # To make it universal the parameters named like below have to be added after self in brackets above
        self.make = '' # the kind of attributes setting with writing in brackets above in class is preferable. (maybe)
        self.model = '' # it is also possible to assign values to objects leaving them as an empty string
        self.year = ''
        self.color = ''
        self.moon_roof = ''
        self.engine_running = ''
    
    # Methods

    def start_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = True 
    
    def stop_engine(self): # method that changes an objects value denoting that it is making someting
        self.engine_running = False


def main(): # function outside of class
    print('Hello from main() function!')
    car1 = Car() # the objects of a class Car were created inside the function main
    car2 = Car()

    # Values
    car1.make = 'Ford' # it is possible to assign values in this fashion too
    car1.model = 'Mustang'
    car1.color = 'Blue'
    car1.year = 2010
    car1.moon_roof = False

    car2.make = 'Tesla'
    car2.model = 'Model 3'
    car2.color = 'Red'
    car2.year = 2020
    car2.moon_roof = True

    # Accessing car1 attributes
    print('Printing car1 details:'.center(50, '-'))
    print('Make: {}'.format(car1.make)) # to access an attribute of an object as in example `car1.model` line of code is necessary
    print('Model: {}'.format(car1.model))
    print('Year: {}'.format(car1.year))
    print('Color: {}'.format(car1.color))
    print('Moon roof: {}'.format(car1.moon_roof))

    # Accessing car2 attributes
    print('Printing car1 details:'.center(50, '-'))
    print('Make: {}'.format(car2.make))
    print('Model: {}'.format(car2.model))
    print('Year: {}'.format(car2.year))
    print('Color: {}'.format(car2.color))
    print('Moon roof: {}'.format(car2.moon_roof))

    # Class Attributes
    print('Class Attributes:'.center(50, '-'))
    print('car1 number of tires:', car1.tires_num)
    print('car1 number of steering wheels', car1.steering_wheel_num)
    Car.steering_wheel_num = 2 # this means that it is possble to change class attribute values for class too
    Car.tires_num = 10 # this means that it is possble to change class attribute values for class too
    print('car2 number of tires:', car2.tires_num)
    print('car2 number of steering wheels', car2.steering_wheel_num)
    print('Car number of tires:', Car.tires_num)
    print('Car number of steering wheels', Car.steering_wheel_num)


if __name__ == '__main__': # function is called if this condition is met
    main()