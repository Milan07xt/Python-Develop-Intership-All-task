from functools import wraps
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        print("fdvxfv")
        return l(*args,**kwargs)
    return b

def a1(a2,b2):
    return a2+b2
a1=a(a1)
a2=int(input("enter a number:"))
b2=int(input("enter a number:"))
print(a1(a2,b2))
