def a(aa):
    return aa%2==0
number=[1,2,3,4,5,6,7,8,9]
b=tuple(filter(a,number))
print(b)


number=[1,2,3,4,5,6,7,8,9]
b=tuple(filter(lambda a: a%2==0 ,number))
print(b)



number=[1,2,3,4,5,6,7,8,9]
b=tuple(filter(a,number))
print(any(b))

number=[1,2,3,4,5,6,7,8,9]
b=tuple(filter(a,number))
print(all(b))


b=["avsx","vSX","dvxz"]
c=[12,3,4,346]
print(dict(zip(b,c)))



b=[12,121,34,56,76,89]
c=[21,32,43,54,65,76]

print(any(i%2==0 for i in b))
print(all(b))

print(any(i%2==0 for i in c))
print(all(c))
