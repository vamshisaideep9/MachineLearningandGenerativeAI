import csv

class Item:

    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []

    def __init__(self, name: str, price: float, quantity=0):

        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)


    def calculate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate

    
    @classmethod
    def instantiate_from_csv(cls):
        with open('python_lll/oops/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point 0
        # for i.e 5.0, 10.0
        if isinstance(num, float):
            #count out the floats that point 0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False
        


    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"



class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity=0, broken_phones = 0):

        #call to super function to have access to all attributes
        super().__init__(
            name, price, quantity
        )

        # Run validations to received arguments
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater than or equal to 0"

        # Assign to self object
        self.broken_phones = broken_phones


        def __repr__(self):
            return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"


phone1 = Phone("jscPhone_v10", 500, 5, 1)

print(Item.all)
print(Phone.all)


