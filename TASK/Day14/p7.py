def a(*args):
    print(args)
    s=0
    for i in args:
        s += i
    return s
num=(2,4,5)
num=[2,3,4,5]
print(a(*num))
