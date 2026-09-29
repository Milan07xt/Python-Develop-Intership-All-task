def a(a1,*args):
    print(a1)
    print(args)
    multiply=1
    for i in args:
        multiply *= i
    return multiply
print(a(2,3,4,5,6,8))
