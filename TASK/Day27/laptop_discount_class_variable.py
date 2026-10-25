class laptop:
    disc=10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        Dis_price=laptop.disc/100*self.price
        return Dis_price
p1=laptop("HP","I5-7gen",46621)
print(p1.brand)
print(p1.model)
print(p1.price)
print(p1.f1())
