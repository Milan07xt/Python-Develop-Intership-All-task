from functools import wraps
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        print("dsvcxxdfzc")
        return l(*args,**kwargs)
    return b
@a
def a1(a2,b2):
    return a2+b2
print(a1(12,45))

from functools import wraps
import time 
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        print("dsvcxxdfzc")
        t1=time.time()
        t2=time.time()
        
        total=t2-t1
        print(total)
        return l(*args,**kwargs)

    return b
@a
def a1(n):
    return [i**2 for i in range(1,n-1)] 
print(a1(1000))

from functools import wraps
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        if all(type(arg)==l for arg in args):
            return l(*args,**kwargs)
        print("svdzxc ")
        return l(*args,**kwargs)
    return b
@a
def a1(a2,b2):
    return a2+b2
print(a1(12,45))
