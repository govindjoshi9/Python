class Dad:
    baskettball =1

class Son(Dad):
    dance = 1
    baskettball = 7
    def isdance(self):
        return f"yes I dance{self.dance}, no of times"

class Grandson(Son):

    dance = 6

    def indance(self):
        return f"Jackson yeah"\
            f"Yes I cab dance{self.dance}, no of times"

darry = Dad()
larry = Son()
Harry = Grandson()

print(Harry.indance())
print(Harry.baskettball)

