def  a(*args):
    print(args)
    
num=(2,3,4,5)
num=[2,3,4,5,6]
print(*num)

def a(num, *args):
    if args: 
        return [i**num for i in args]
    else:
        return "You didn't pass any args" 
nums = [1,2,3] 
print(a(3, *nums)) 


def a(num, *args):
    a1= []
    for i in args:
        a1.append(i ** num)
    return a1
nums = [4,5,6,7]
print(a(3, *nums))
