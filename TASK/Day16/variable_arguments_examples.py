def a(*args):
    for i in args:
        print(i)
a(24,25)

def a(*args):
    m=1
    for i in args:
        m *= i
    return m
print(a(5,56,5))

def a(*args):
    m=0
    for i in args:
        m += i
    return m
print(a(5,56,5))

def a(*args):
    m=0
    for i in args:
        m -= i
    return m
print(a(5,56,5))


def a(*kwargs):
    print(kwargs)
a("dfsv","dvszx")


def a(**kwargs):
    print(kwargs)
    print(type(kwargs))

a(name="svzX", age=54)


def a(*args):
    even = []
    for i in args:
        if i % 2 == 0:
            even.append(i)
        else:
            print("odd:", i)
    print(even)
    return even
a(12,20,30)


def a(*args):
    multiply=1
    for i in args:
        multiply *=i
    return multiply
print(a(12,401,20))


def a(num,*args):
    multiply=1
    print(num)
    for i in args:
        multiply *=i
    return multiply
print(a(12,401,200,20))

a1=lambda a,b: a*b
print(a1(20,30))

