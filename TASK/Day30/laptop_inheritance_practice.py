class phone:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        return f"{self.brand} {self.model}  {self.price}"
class laptop1(laptop):
    def __init(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        return f" {self.brand}  {self.model}  {self.price}"
p1=laptop("HP","I7-9Gen",65000)
p2=laptop1("Dell","I5-8Gen",50000)
print(p1.f1())
print(p2.f1())
