class Location(object):
    """class to create a Location"""

    def __init__(self, city, postoffice):
        """
        Description
        """
        self.city, self.postoffice = city, postoffice


class Item(object):
    """class to create an Item"""

    def __init__(self, name, price):
        """
        Description
        """
        self.name, self.price = name, price

    def __str__(self):
        """
        Return: a string with name and price for this item

        """
        return "{} - {}".format(self.name, self.price)


class Vehicle(object):
    """class to create a Vehicle"""

    def __init__(self, vehicleNo):
        """
        Description
        """
        self.vehicleNo, self.isAvailable = vehicleNo, True