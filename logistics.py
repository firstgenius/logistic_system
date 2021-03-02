'''
This module realizes logistics system.
'''


from typing import List
import random


class Location:
    '''
    The Location represents the city and the postoffice.
    '''
    def __init__(self, city: str, postoffice: int):
        '''
        Initialize variables of Location.

        >>> office_53 = Location('Lviv', 53)
        >>> office_53.city
        'Lviv'
        >>> office_53.postoffice
        53
        '''

        self.city = city
        self.postoffice = postoffice


class Item:
    '''
    The Item represents the name and price of the product.
    '''
    def __init__(self, name: str, price: float):
        '''
        Initialize variables of Item

        >>> flowers = Item('flowers',110)
        >>> flowers.name
        'flowers'
        >>> flowers.price
        110
        '''

        self.name = name
        self.price = price

    def __str__(self) -> str:
        '''
        Returns a string to represent the name and price of the product.

        >>> flowers = Item('flowers',110)
        >>> print(flowers)
        flowers cost(s) 110 UAH.
        >>> cake = Item('cake',230)
        >>> print(cake)
        cake cost(s) 230 UAH.
        '''
        return f'{self.name} cost(s) {self.price} UAH.'


class Vehicle:
    '''
    The Vehicle represents the vehicleNo and whether it is available.
    '''
    def __init__(self, vehicleNo: int, isAvailable = True):
        '''
        Initialize variables of Vehicle.

        >>> vehicle_15 = Vehicle(15, True)
        >>> vehicle_15.vehicleNo
        15
        >>> vehicle_15.isAvailable
        True
        '''

        self.vehicleNo = vehicleNo
        self.isAvailable = isAvailable


class Order:
    '''
    Processes and contains order information
    '''
    def __init__(self, user_name: str, city: str, postoffice: int, items: List[Item]):
        '''
        Initialize variables of Order.

        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> my_order.user_name
        'Oleg'
        >>> my_order.city
        'Lviv'
        >>> my_order.postoffice
        53
        '''
        self.orderId = random.randint(100000000, 999999999)
        self.user_name = user_name
        self.city = city
        self.postoffice = postoffice
        self.items = items


    def __str__(self) -> str:
        '''
        Returns a string to represent the order number.
        '''

        return f'Your order number is {self.orderId}.'

    def calculateAmount(self) -> int:
        '''
        Calculates the amount of items.

        >>> my_items = [Item('book',110), Item('chupachups',44)]
        >>> my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
        >>> my_order.calculateAmount()
        2
        '''
        return len(self.items)

    def assignVehicle(self, vehicle: Vehicle):
        '''
        Sends vehicle on work for delivery and make his 'flag' False.
        '''
        self.vehicle = vehicle
        self.vehicle.isAvailable = False


class LogisticSystem:
    '''
    This module realizes logistics system.
    '''
    def __init__(self, vehicles: List[Vehicle]):
        '''
        Initialize variables of LogisticSystem.

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> logSystem.vehicles[0].isAvailable
        True
        >>> logSystem.vehicles[1].vehicleNo
        2
        '''

        self.orders = []
        self.vehicles = vehicles

    def placeOrder(self, order: Order):
        '''
        Checks if there are free vehictes to deliver your package.

        >>> vehicles = []
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
        >>> my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
        >>> logSystem.placeOrder(my_order3)
        'There is no available vehicle to deliver an order.'
        '''

        for car in self.vehicles:
            if car.isAvailable:
                order.assignVehicle(car)
                car.isAvailable = False
                self.orders.append(order)
                return
        return 'There is no available vehicle to deliver an order.'

    def trackOrder(self, orderId: int) -> str:
        '''
        Checks whether there is package with such ID. If there is,
        gives you info about it.
        '''

        for order in self.orders:
            print(order.orderId)
            if orderId == order.orderId:
                return f'Your order #{order.orderId} is sent to\
 {order.city}. Total price: {order.items} UAH.'
        return 'No such order.'
