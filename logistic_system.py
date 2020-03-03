from loc_item_vehicle import Vehicle, Item, Location
from order import Order, Sender

from LogisticSystem.price_for_transportion import price_for_transport


class LogisticSystem(object):
    """class to create a Logistic System"""

    def __init__(self, vehicles):
        """
        Description
        """
        self.vehicles = vehicles
        self.orders = []
        self.senders = []

    def placeOrder(self, order: Order):
        """
        Assign Vehicle to this order

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        Your order number is 53797691
        >>> logSystem.placeOrder(my_order)

        """
        order.assignVehicle(self.vehicles)
        self.orders.append(order)
        if order.vehicle == 0:
            return "There is no available vehicle to deliver an order."

    def trackOrder(self, orderId):
        """
        Tell if this order can be made and say total price for all items

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        Your order number is 53797691
        >>> logSystem.placeOrder(my_order)

        >>> logSystem.trackOrder(53797691)
        'Your order #53797691 is sent to Lviv. Total price: 154 UAH.'
        """
        for order in self.orders:
            if order.orderId == str(orderId) and order.vehicle != 0:
                city = order.city
                price = order.calculateAmount()
                return "Your order #{} is sent to {}." \
                       " Total price: {} UAH.".format(orderId, city, price)

        return "No such order."

    def add_sender_to_db(self, order: Order, sender: Sender):
        """
        Add sender to Logistic System
        """
        self.senders.append([order, sender])

    def make_price_for_transportation(self, orderId):
        """
        Make a price for transportation based on destination between from_city and city

        >>> vehicles = [Vehicle(1), Vehicle(2)]
        >>> logSystem = LogisticSystem(vehicles)
        >>> my_items = [Item('book', 110), Item('chupachups', 44)]
        >>> my_order = Order('Oleg', 'Lviv', 53, my_items)
        Your order number is 53797691
        >>> logSystem.placeOrder(my_order)

        >>> logSystem.trackOrder(53797691)
        'Your order #53797691 is sent to Lviv. Total price: 154 UAH.'
        >>> sender = Sender("Denys", "Lokhvytsia")
        >>> logSystem.add_sender_to_db(my_order, sender)
        >>> logSystem.make_price_for_transportation(53797691)
        'Denys, your price for transportation from Lokhvytsia to Lviv is 300 UAH, distance - 740.659 km'
        """
        for sender in self.senders:
            if sender[0].orderId == str(orderId) and sender[0].vehicle != 0:
                distance = price_for_transport(sender[1].from_location, sender[0].city)
                if distance <= 50:
                    price_transport = 100

                elif 50 < distance <= 100:
                    price_transport = 200

                elif 100 < distance:
                    price_transport = 300

                return "{}, your price for transportation " \
                       "from {} to {} is {} UAH, distance - {} km".format(sender[1].user_name, sender[1].from_location,
                                                        sender[0].city, price_transport, round(distance, 3))

        return "No such order."


if __name__ == '__main__':
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order('Oleg', 'Lviv', 53, my_items)
    print(logSystem.placeOrder(my_order))
    print(logSystem.trackOrder(53797691))
    print()
    my_items2 = [Item('flowers', 11), Item('shoes', 153), Item('helicopter', 0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    print(logSystem.placeOrder(my_order2))
    print(logSystem.trackOrder(51657991))
    print()
    my_items3 = [Item('coat', 61.8), Item('shower', 5070), Item('rollers', 700)]
    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    print(logSystem.placeOrder(my_order3))
    print(logSystem.trackOrder(49797591))
    print()
    sender = Sender("Denys", "Lokhvytsia")
    logSystem.add_sender_to_db(my_order, sender)
    print(logSystem.make_price_for_transportation(53797691))
