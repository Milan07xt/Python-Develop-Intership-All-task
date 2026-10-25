class person:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name=l_name
    def a1(self):
        return f"{self.f_name}   {self.l_name}"
a=person("dsvxcz","dczx")
print(a.a1())
b=person("dszxc","dsvcx")
print(b.a1())
c=person("dsv","fdvzx")
print(c.a1())
