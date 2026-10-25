class person:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def f1(self):
        return f"{self.name}   {self.price}"

p1=person("fdzxv",45664)
p2=person("sdxgds",3464)
print(p1.name)
print(p1.price)
print(person.f1(p1))
