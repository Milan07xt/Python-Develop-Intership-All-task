class laptop:
    def __init__(self,brand,model,ram,price):
        self.brand=brand
        self.model=model
        self.ram=ram
        self.price=price
    def f1(self):
        return f"{self.brand}  {self.model} {self.ram}  {self.price}"
    def f2():
        print("dgsvcx")
    
p1=laptop("Hp","I5-7Gen","512GB",45000)
print(p1.f1())
print(p1.__dict__)
p1._laptop_price=450000
print(p1._laptop_price)
print(laptop.f2())
p2=p1
print(p2.f1())
