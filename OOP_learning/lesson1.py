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


def main(): # function outside of class
    print('Hello from main() function!')
    car1 = Car('Ford', 'Mustang', 2011, 'Blue') # the obhects of a class Car were created inside the function main
    car2 = Car('Tesla', 'Model 3', 2021, 'Red', True)

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
    print('car2 number of tires:', car2.tires_num)
    print('car2 number of steering wheels', car2.steering_wheel_num)
    print('Car number of tires:', Car.tires_num)
    print('Car number of steering wheels', Car.steering_wheel_num)


if __name__ == '__main__': # function is called if this condition is met
    main()