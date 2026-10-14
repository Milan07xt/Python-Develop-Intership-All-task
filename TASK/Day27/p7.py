class person:
    c1=0
    def __init__(self,f_name,l_name,age):
        self.f_name=f_name
        self.l_name=l_name
        self.age=age
    @classmethod
    def count_person(cls):
        return f"You have created {cls.c1} instances"
    def full_name(self):
        return f"{f_name}  {l_name}"
    def f1(self):
        return self.age>18
p1=person("zcx","advz",45)
print(p1.f_name)
print(p1.l_name)
print(p1.age)
print(person.count_person())
