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
        return f"{self.brand}  {self.model}  {self.price}"
class laptop2(laptop):
    def __init__(self,brand,model,Ram,price):
        self.brand=brand
        self.model=model
        self.Ram=Ram
        self.price=price
    def f3(self):
        return f"{self.brand}  {self.model} { self.Ram} {self.price}"
class laptop3(laptop):
    def __init__(self,brand,model,Ram,price,generation):
        self.brand=brand
        self.model=model
        self.Ram=Ram
        self.price=price
        self.generation=generation
    def f4(self):
        return f"{self.brand}  {self.model} { self.Ram} {self.price} {self.generation}"
p1=laptop("Hp",45000)
p2=laptop1("Hp","I5-7Gen",45000)
p3=laptop2("Hp","I5-7Gen","512GB",45000)
p4=laptop3("Hp","I5-7Gen","512GB",45000,7)
print(p1.f1())
print(p2.f2())
print(p3.f3())
print(p4.f4())
