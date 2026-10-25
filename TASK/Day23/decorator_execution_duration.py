from functools import wraps
import time
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        t1=time.time()
        a3=l(*args,**kwargs)
        t2=time.time()
        total=t2-t1
        print(total)
        return a3
    return b
@a
def a1(n):
    return [i**2 for i in (1,n+1)]
a1(1000)

from functools import wraps
import time

def a(l):
    @wraps(l)
    def b(*args, **kwargs):
        t1 = time.time()
        a3 = l(*args, **kwargs)
        t2 = time.time()

        total = t2 - t1
        print("Execution time:", total, "seconds")

        return a3
    return b

@a
def a1(n):
    return [i**2 for i in range(1, n+1)]
print(a1(1000))
