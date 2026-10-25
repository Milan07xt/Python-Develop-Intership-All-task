class laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name=brand_name
        self.model_name=model_name
        self.price=price
p1=laptop("HP","I5- 7gen",45220)
p2=laptop("Dell","I5- 8gen",48800)
p3=laptop("Lenovo","I7- 7gen",50000)
print(p1)
print(p2)
print(p3)
print(p1.brand_name)
print(p1.model_name)
print(p1.price)
print(p2.brand_name)
print(p2.model_name)
print(p2.price)
print(p3.brand_name)
print(p3.model_name)
print(p3.price)
