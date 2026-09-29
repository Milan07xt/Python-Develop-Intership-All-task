def a(*args):
    print(args)
    a1=0
    for i in args:
        a1 +=i
    return a1
print(a(2,3,4,5,6))    


def a(*args):
    for i in args:
        print(i)
print(a(2,3,4,5,6))    


def a(*args):
    for i in args:
        if i % 2==0:
            print(i)
print(a(2,3,4,5,6))    

def a(*args):
    for i in args:
        if i % 2==1:
            print(i)
print(a(2,3,4,5,6))    

def largest(*args):
    m = args[0]

    for i in args:
        if i > m:
            m = i

    return m

print(largest(10, 25, 5, 40, 15))


def s1(*args):
    s = args[0]

    for i in args:
        if i < s:
            s= i

    return s

print(s1(10, 25, 5, 40, 15))


def s1(*args):
    s = args[0]

    for i in args:
        if i < s:i=s.count(args)

    return s

print(s1(10, 25, 5, 40, 15))
