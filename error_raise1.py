class Mobile:
    def __init__(self,name):
        self.name = name 

class Mobilestore:
    def __init__(self):
        self.mobile = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile,Mobile):
            self.mobile.append(new_mobile)
        else:
            raise TypeError("new mobile should be object of mobile class")
        self.mobile.append(new_mobile)


opeplus = Mobile('one plus 6')
samsung = 'samsung galaxy s9'

mobostore = Mobilestore()
# print(mobostore.mobile)
mobostore.add_mobile(opeplus)
print(mobostore.mobile)
