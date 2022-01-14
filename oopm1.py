class Phone:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self._price = max(price,0)

        self._price = price
        self.complet_spacifer = f"{self.brand} {self.model} and price"

    def make_a_call(self,phone_no):
        print(f"calling{phone_no}...")

    def full_name(self):
        return f"{self.brand} {self.model}"

phone1 = Phone('Nokia', '1100',-1000)
print(phone1.brand)
print(phone1.model)
print(phone1._price)
        
