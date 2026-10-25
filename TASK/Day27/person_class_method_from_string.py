class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def a1(cls,data):
        name,age=data.split()
        return cls(name,int(age))
p1=person("azcx",45)
print(p1.name)
print(p1.age)
