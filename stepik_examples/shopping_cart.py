class Item:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __str__(self):
        return f'{self.item}, {self.price}$'
    

class ShoppingCart:
    def __init__(self, items=[]):
        self.items = items

    def add(self, good: Item):
        self.items.append(good)

    def total(self):
        res = [i.price for i in self.items]
        return sum(res)
    
    def remove(self, item_name):
        item_indexes = []
        for i in range(len(self.items)):
            if self.items[i].item == item_name:
                item_indexes.append(i)
        for i in reversed(item_indexes):
            del self.items[i]


    def __str__(self) -> str:
        if self.items:
            return '\n'.join(map(str, self.items))
        else:
            return ''

# tests

print('TEST_1:')
item1 = Item('Yoga Mat', 130)
item2 = Item('Flannel Shirt', 22)

print(item1)
print(item2)

print('TEST_2:')
shopping_cart = ShoppingCart([Item('Yoga Mat', 130)])

shopping_cart.add(Item('Flannel Shirt', 22))
print(shopping_cart)
print(shopping_cart.total())

print('TEST_3:')
shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])

shopping_cart.remove('Yoga Mat')
print(shopping_cart)
print(shopping_cart.total())

print('TEST_4:')
shopping_cart = ShoppingCart([Item('Banana', 100), Item('Apple', 120), Item('Orange', 110), Item('Tomato', 180), Item('Cucumber', 150)])

shopping_cart.add(Item('Banana', 100))
print(shopping_cart)
print(shopping_cart.total())

shopping_cart.remove('Banana')
print(shopping_cart)
print(shopping_cart.total())

# TEST_5:
shopping_cart = ShoppingCart()

print(shopping_cart)
