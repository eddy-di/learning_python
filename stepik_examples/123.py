class Versioned:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        attr_name = self._get_attribute_name(instance)
        if attr_name in instance.__dict__:
            return instance.__dict__[attr_name][-1]
        raise AttributeError('Атрибут не найден')
    
    def __set__(self, instance, value):
        attr_name = self._get_attribute_name(instance)
        current_value = self._get_current_value(instance, attr_name)
        
        if current_value is not None:
            instance.__dict__[attr_name].append(value)
        else:
            instance.__dict__[attr_name] = [value]

    def _get_attribute_name(self, instance):
        for attr_name, attr_value in instance.__class__.__dict__.items():
            if attr_value is self:
                return attr_name
        return None

    def _get_current_value(self, instance, attr_name):
        if attr_name in instance.__dict__:
            return instance.__dict__[attr_name][-1]
        return None

    def get_version(self, instance, n):
        attr_name = self._get_attribute_name(instance)
        if attr_name in instance.__dict__ and n >= 1 and n < len(instance.__dict__[attr_name]):
            return instance.__dict__[attr_name][n]
        return None

    def set_version(self, instance, n):
        attr_name = self._get_attribute_name(instance)
        if attr_name in instance.__dict__ and n >= 1 and n < len(instance.__dict__[attr_name]):
            current_value = instance.__dict__[attr_name][n]
            instance.__dict__[attr_name] = [current_value]

class MyClass:
    value = Versioned()


# Usage
obj = MyClass()

# Set and get values
obj.value = 1
obj.value = 2
obj.value = 3

print(obj.value)  # Output: 3

# Get versions
print(obj.value.get_version(0))  # Output: 1
print(obj.value.get_version(1))  # Output: 2
print(obj.value.get_version(2))  # Output: 3

# Set version
obj.value.set_version(1)
print(obj.value)  # Output: 2
