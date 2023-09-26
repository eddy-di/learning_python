class Example:
    class_attribute = "example atribute"

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

ex = Example('atrs')

print(ex.__dict__)