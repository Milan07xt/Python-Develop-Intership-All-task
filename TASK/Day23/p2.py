def a(l):
    def b(*args,**kwargs):
        print("dvcxdzvc ")
        return l(*args,**kwargs)
    return b
@a
def a1(a2,b2):
    return a2+b2
print(a1(12,56))

