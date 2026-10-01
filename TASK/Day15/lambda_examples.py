
a1=lambda a,b: a+b
print(a1(10,20))

a1=lambda a,b: a*b
print(a1(10,20))


a=int(input("enter a number:"))
b=int(input("enter a number:"))
a1=lambda a,b: a+b
print(a1(a,b))


def a(aa):
        if aa %2==0:
            return aa
        else:
            print("odd")
print(a(453))

def f(a):
    if len(a) >5:
        return True
    else:
        return False
print(f("safhgdg"))


f=lambda a: True if len(a)>5 else False
print(f("savzx"))

l_c=lambda s:s[-1]
print(l_c("ascvXZ"))
