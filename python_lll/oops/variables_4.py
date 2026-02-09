class Item:

    pay_rate = 0.8 #The pay rate after 20% discount.

    def __init__(self, name: str, price: float, quantity:float):

        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Qunatity {quantity} is not greater than or equal to 0"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity

    
    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100, 0)
item2 = Item("Laptop", 1000, 3)


item1.apply_discount()
print(item1.price)


item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


# print(Item.pay_rate) #access from class level
# print(item1.pay_rate) #access from instance attribute


# print(Item.__dict__)  #All attributes for class level
# print(item1.__dict__) #All attributes for instance level


 