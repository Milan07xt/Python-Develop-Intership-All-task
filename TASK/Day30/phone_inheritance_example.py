class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        return f"{self.brand} {self.model}  {self.price}"
class phone1(phone):
    def __init(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        return f"{self.brand}  {self.model}  {self.price}"
p1=phone("Iphone14","5G",65000)
p2=phone1("Iphone16","5G",50000)
print(p1.f1())
print(p2.f1())
