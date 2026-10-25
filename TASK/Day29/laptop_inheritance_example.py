class laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def p1(self):
        return f"{self.brand} {self.price}"
class laptop1(laptop):
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def f1(self):
        return f"{self.brand}  {self.model}  {self.price}"
p2=laptop("HP",55000)
print(p2.p1())
p3=laptop1("HP","I5-7Gen",45000)
print(p3.p1())
print(p3.f1())
