class person:
    def __init__(self,brand,model_name,price):
        self.brand=brand
        self.model_name=model_name
        self.price=price
    def f1(self,num):
        d=(num/100)*self.price
        return self.price - d
p1=person("HP","faszx",46400)
print(p1.brand)
print(p1.model_name)
print(p1.price)
print(p1.f1(10))
p2=person("Dell","advszc",45000)
print(p2.brand)
print(p1.f1(50))
