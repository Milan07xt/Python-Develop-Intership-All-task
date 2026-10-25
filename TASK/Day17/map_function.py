num=[12,5,4,6,123]
def s(a):
    return a**2
print(list(map(s,num)))

num=(12,5,4,6,123)
def s(a):
    return a**2
print(tuple(map(s,num)))

name=["aadsaa","bbb","ccc"]
a=list(map(len,name))
print(a)

l=["aaa","bbb","ccc"]
a=list(map(list,l))
print(a)

num1=[1,2,3]
num2=[4,5,6]
l=map(lambda num1,num2:num1+num2, num1,num2)
print(list(l))


num1=[1,2,3]
num2=[4,5,6]
l=map(lambda num1,num2:num1+num2, num1,num2)
print(tuple(l))

num1=[1,2,3]
num2=[4,5,6]
l=map(lambda i:i*2 ,num1+ num2)
print(list(l))

num1 = [1, 2, 3]
num2 = [4, 5, 6]
l = map(lambda i: i * 2, num1 + num2)
print(list(l))
