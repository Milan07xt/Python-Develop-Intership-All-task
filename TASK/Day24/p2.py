def a(l):
    def b(*args,**kwargs):
        print("fdsfdszvx")
        return l(*args,**kwargs)
    return b
@a
def a1(a2,b2):
    return a2+b2
print(a1(12,65))

def a(l):
    def b():
        l=()
        print("fdsfdszvx")
        return l
    return b
@a
def a1():
    print("fadvzxv")
a2=a(a1)
print(a2())
