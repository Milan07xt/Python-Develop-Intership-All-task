class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def f1(self):
        return f"{self.name}   {self.age}"
p1=person("sdvzc",45)
print(p1.name)
print(p1.age)
print(person.f1(p1))


class person1:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    def f1(self):
        return f"{self.f_name}   {self.l_name}"
p1=person1("vzxc","cvx")
print(p1.f_name)
print(p1.l_name)
print(person1.f1(p1))
