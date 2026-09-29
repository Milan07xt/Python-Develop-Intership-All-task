def s(*args):
    total=0
    for i in args:
        if i %2==0:
            total += i
    return total
print(s(1,2,3,4,5,6,6,7,8,9))
