# What is this ?

This is a logistic system like in postoffice, where you can input your items, get total amount of them, get to know if 
your order can be made based on if vehicle is free to transport your order. Also you can get to know total sum of your parcel transportation
based on distance between from_city and city. where you send it.  

If you will print in logistic_system.py:
    
    ```
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book', 110), Item('chupachups', 44)]
    my_order = Order('Oleg', 'Lviv', 53, my_items)
    print(logSystem.placeOrder(my_order))
    print(logSystem.trackOrder(53797691))
    print()
    ```

    ```
    sender = Sender("Denys", "Lokhvytsia") - name, from_location
    logSystem.add_sender_to_db(my_order, sender)
    print(logSystem.make_price_for_transportation(53797691))
    ```
    



You will get:
    
    ```
    Your order number is 53797691
    None
    Your order #53797691 is sent to Lviv. Total price: 154 UAH.

    Denys, your price for transportation from Lokhvytsia to Lviv is 300 UAH, distance - 740.659 km
    ```
    

#My main work 
I add class Sender and two functions in logistic_system.py:
    
    ```
    def add_sender_to_db(self, order: Order, sender: Sender):
        """
        Add sender to Logistic System
        """
        self.senders.append([order, sender])
    ```

    ```
    def make_price_for_transportation(self, orderId):
        """
        Make a price for transportation based on destination between from_city and city
    ```

The UML diagram you can find here in __Herasymuk_Lab_4 Diagram.pdf__