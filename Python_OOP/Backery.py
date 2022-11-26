# Welcome to this Mini Project.

# Now you are hired to fix an object-oriented program that is essential for your local bakery. The previous developer added many bugs and errors to the program on purpose due to conflicts with the manager.

# The store owner is extremely worried because these errors could seriously affect her business and sales.

# But you can save the day by fixing the classes.

#----------BUG FIXING---------------------------------------

# class Donut
 
#     def _ini__(flavor, toppings, filling, size):
#         self.flavor = flavor
#         self.toppings = toppings
#         self.filling = filling
#         size = self.size

class Donut:
 
    def _init__(self, flavor, toppings, filling, size):
        self.flavor = flavor
        self.toppings = toppings
        self.filling = filling
        self.size = size


#----------BUG FIXING---------------------------------------

# class Customer:
 
#     def _init_(self, name, age address, favorite_dessert)
#         self.name = name
#         self.age = age
#         self.address = address
#         favorite_dessert= self.favorite_dessert


class Customer:
 
    def _init_(self, name, age, address, favorite_dessert):
        self.name = name
        self.age = age
        self.address = address
        self.favorite_dessert= favorite_dessert


#----------BUG FIXING---------------------------------------

# Cake:
#     __init__(self, flavor, price, quality):
#         self.flavor = flavor
#         self.price = price
#         self.quality = quality

class Cake:
    def __init__(self, flavor, price, quality):
        self.flavor = flavor
        self.price = price
        self.quality = quality

