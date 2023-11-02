class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        # Check some condition (e.g., if value meets a specific condition)
        if self.value > 10:
            # ANSI escape code for red text
            red_color_code = "\033[91m"
            # ANSI escape code to reset text color
            reset_color_code = "\033[0m"
            
            # Return the formatted string
            return f"{red_color_code}Value: {self.value}{reset_color_code}"
        else:
            return f"Value: {self.value}"

# Create instances of MyClass
obj1 = MyClass(5)
obj2 = MyClass(15)

# Print the instances
print(obj1)  # Output will be normal text
print(obj2)  # Output will be red text for values greater than 10
