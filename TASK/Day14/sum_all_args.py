#Intro to * args

def s(*args):
    total=0
    for i in args:
        total += i
    return total
print(s(1,2,3,4,6))
