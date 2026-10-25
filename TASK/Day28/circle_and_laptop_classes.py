class circle:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def a1(self):
        return 2*circle.pi*self.radius
a=circle(10)
print(a.a1())

class laptop:
    disc=10
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def all(self):
        a2=self.price*laptop.disc/100
        return a2
a=laptop("HP","I5-Gen",45660)
print(a.all())
laptop.disc=50
print(a.all())
