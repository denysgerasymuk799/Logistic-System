from loc_item_vehicle import Vehicle, Item, Location


class Order(object):
    """class to create an Order"""

    def __init__(self, user_name, location, postoffice, items):
        """
        Description
        """
        self.postoffice, self.user_name, self.location, self.items =\
            postoffice, user_name, location, items

        self.location = location
        self.city = location
        code = ''
        for element in [self.postoffice, self.user_name, self.location, self.items]:
            code += str(ord(str(element)[0]))
        self.orderId = code
        print("Your order number is {}".format(self.orderId))

    def __str__(self):
        """
        Return: a string with name and location where you want to send a parcel

        """
        return "{} wants to send in {} his/her items".format(self.user_name, self.location)

    def calculateAmount(self):
        """
        Calculate an amount of all items

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        Your order number is 53797691
        >>> my_order.calculateAmount()
        154
        """
        amount = 0
        for item in self.items:
            amount += item.price

        return amount

    def assignVehicle(self, vehicles):
        """
        int -> None
        Return: put a vehicle with a vehicleNo to this order
        or put 0 - if all vehicles are false

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        Your order number is 53797691
        >>> my_order.calculateAmount()
        154
        >>> my_order.assignVehicle(vehicles)
        >>> my_order.vehicle
        1
        """
        self.vehicle = 0
        for vehicle in vehicles:
            if vehicle.isAvailable:
                self.vehicle = vehicle.vehicleNo
                vehicle.isAvailable = False
                break


class Sender(object):
    """class to get information about the sender"""

    def __init__(self, user_name, from_location):
        """
        Description
        """
        self.user_name, self.from_location =\
            user_name, from_location


if __name__ == '__main__':
    vehicles = [Vehicle(1), Vehicle(2)]
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order('Oleg', 'Lviv', 53, my_items)
    print(my_order.calculateAmount())
    print(my_order)
    my_order.assignVehicle(vehicles)
    print(my_order.vehicle)
    print()
    my_items = [Item('book', 11), Item('chupachups', 44)]
    my_order2 = Order('Oleg', 'Kyiv', 55, my_items)
    print(my_order2.calculateAmount())
    print(my_order2)
    my_order2.assignVehicle(vehicles)
    print(my_order2.vehicle)