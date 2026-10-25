class laptop:
    disc=10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        off_price= self.disc / 100*self.price
        return self.price - off_price
p1=laptop("HP","I5-7Gen",45000)
print(p1.brand)
print(p1.model)
print(p1.price)
print(p1.f1())
p1.disc=50
print(p1.f1())
print(p1.__dict__)
