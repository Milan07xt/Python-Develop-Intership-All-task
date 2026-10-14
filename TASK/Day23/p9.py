from functools import wraps
def a(l):
    @wraps(l)
    def b(*args,**kwargs):
        if all(type(args)== l for arg in args ):
            return l(*args,**kwargs)
        print("zvxbzgdxb")
    return b
@a
def a1(*args):
    a2=''
    a2=0
    for i in args:
        a+=1
    return a2
print(a1("zvxzvx","szvf"))
    
