def a(int1,int2):
    add = int1 + int2
    multiply = int1 * int2
    return add, multiply
add, multiply=a(20,30)
print(add)
print(multiply)

def b(a,b1):
    sub=a-b1
    division=a%b1
    return sub ,division
sub,division=b(10,20)
print(sub)
print(division)
