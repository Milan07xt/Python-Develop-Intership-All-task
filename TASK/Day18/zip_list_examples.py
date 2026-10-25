a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=list(zip(a,b))
print(c)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=tuple(zip(a,b))
print(c)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=dict(zip(a,b))
print(c)

a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(tuple(zip(a,b)))

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=["zxv","vcxz","gdsv"]
print(list(zip(a,b,c)))
print(tuple(zip(a,b,c)))
print(dict(zip(a,b,c)))#Error
