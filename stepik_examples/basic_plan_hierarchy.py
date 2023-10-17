class BasicPlan:
    can_stream = True
    can_download = True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices = 1
    price = '8.99$'


class SilverPlan(BasicPlan):
    has_HD = True
    has_UHD = False
    num_of_devices = 2
    price = '12.99$'


class GoldPlan(BasicPlan):
    has_HD = True
    has_UHD = True
    num_of_devices = 4
    price = '15.99$'


# tests

print('TEST_1:')
print(BasicPlan.can_stream)
print(BasicPlan.can_download)
print(BasicPlan.has_SD)
print(BasicPlan.has_HD)
print(BasicPlan.has_UHD)
print(BasicPlan.num_of_devices)
print(BasicPlan.price)

print('TEST_2:')
print(SilverPlan.can_stream)
print(SilverPlan.can_download)
print(SilverPlan.has_SD)
print(SilverPlan.has_HD)
print(SilverPlan.has_UHD)
print(SilverPlan.num_of_devices)
print(SilverPlan.price)

print('TEST_3:')
print(GoldPlan.can_stream)
print(GoldPlan.can_download)
print(GoldPlan.has_SD)
print(GoldPlan.has_HD)
print(GoldPlan.has_UHD)
print(GoldPlan.num_of_devices)
print(GoldPlan.price)

print('TEST_4:')
print(issubclass(SilverPlan, BasicPlan))
print(issubclass(GoldPlan, BasicPlan))