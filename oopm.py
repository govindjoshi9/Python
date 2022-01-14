class Laptop:
    discount_percent = 10
    def __init__(self,brand , name, price):
        self.brand = brand
        self.name = name 
        self.price = price
        self.laptop_name = brand + " " + name
    def apply_discount(self):
        # self.price
        off_price = (self.discount_percent/100)*self.price
        return self.price - off_price

laptop1 = Laptop("hp", 'au114tx',63000)
laptop2 = Laptop("apple", "mac book", 230000)
laptop2.discount_percent =50
print(laptop2.__dict__)
print(laptop2.apply_discount())
# print(laptop1.name)
# print(laptop1.laptop_name)
print(laptop1.apply_discount())

