class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        return "This is animal sound"

class Dog(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread = bread

class Cat(Animal):
    def __init__(self,name,bread):
        super().__init__(name)
        self.bread = bread

doggy = Dog("bonny", "pug")
print(doggy.sound())