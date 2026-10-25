class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def f1(self):
        return f"{self.brand}  {self.price}"
class laptop1(laptop):
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f2(self):
        return f"{self.brand}  {self.model} {self.price}"
class laptop2(laptop):
    def __init__(self,brand,model,ram,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.price=price
    def f3(self):
        return f"{self.brand} {self.model} {self.ram} {self.price}"
laptop1=laptop2("Hp","I5-7Gen","512GB",45000)
print(laptop1.f1())
