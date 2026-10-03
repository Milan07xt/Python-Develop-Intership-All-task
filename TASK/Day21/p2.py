def a():
    print("safzxc")
a()
def a1(a):
    return a*2
print(a1(4))

def aa(a):
    return a*2
l=[1,2,3,4,5,6,7,8]
print(list(map(aa,l)))
print(list(map(lambda a:a**2,l)))

def a(aa):
    return aa*2
l=["faszxv","dvxz","vxz",21,45,16]
print(list(map(a,l)))

def aa(a):
    return a*2
l=[1,2,3,4,5,6,7,8]
def a(func,l):
    n=[]
    for item in l:
        n.append(func(item))
    return n
print(a(aa,l))

def a():
    def aa():
        print("dxzsdzc")
    return aa()
a()

def b():
    def ba():
        print("zxvgvxc")
    return ba
a1=b()
a1()
