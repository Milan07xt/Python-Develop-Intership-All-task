class person:
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def calc_r(self):
        return  2*self.pi*self.radius
p1=person(5)
print(p1.calc_r())
