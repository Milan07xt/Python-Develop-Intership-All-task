from functools import wraps
def a(l):
    def b(*args,**kwargs):
        if all(type(arg)==int for arg in args):
            return l(*args,**kwargs)
        print("afsvzx")
    return b
@a
def a1(a2,b2):
    return a2+b2
print(a1(4656,56))
print(a1(66,"dvaz"))
