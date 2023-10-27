from enum import Flag, auto


class OrderStatus(Flag):
    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()

# TESTS

print('TEST_1:')
order_status = OrderStatus(0)
order_status |= OrderStatus.ORDER_PLACED

if OrderStatus.ORDER_PLACED in order_status:
    print('Заказ оформлен!')
    
order_status |= OrderStatus.PAYMENT_RECEIVED

if OrderStatus.PAYMENT_RECEIVED in order_status:
    print('Оплата получена!')
    
order_status |= OrderStatus.SHIPPING_COMPLETE

if OrderStatus.SHIPPING_COMPLETE in order_status:
    print('Доставка завершена!')

print('TEST_2:')
print(OrderStatus.ORDER_PLACED.value)
print(OrderStatus.PAYMENT_RECEIVED.value)
print(OrderStatus.SHIPPING_COMPLETE.value)

print('TEST_3:')
for order in OrderStatus:
    print(order)