a=[1,2,3,4,5,6,7,8,9]
print(min(a))
print(max(a))


a=["asvf","dvxz","vda","fascvzx"]
print(min(a))
print(max(a))
print(sorted(a))
a.sort()
print(a)

a=[1,2,3]
b=[4,5,6]
aa=lambda a,b:a+b 
print(aa(12,34))

a1=lambda a,b:a*b
print(a1(12,20))

a2=lambda a,b:a/b
print(a2(20,30))


a=["af","fadsvz","afsdvz"]
print(a)
a.append("asffsa")
print(a)

a.remove("af")
print(a)

a.pop()
print(a)

a=(12,23,45,6,57,89,12)
print(a)

a={
    "dvsz":465,
    "dvsvdzx":56
    }
print(a)

a.update({"vdszx":656,"avzx":586})
print(a)

a=["dsfvz","sacfxz","saczx"]
b=["dcz","cxz","xz scaxZ"]
print(dict(zip(a,b)))

a=[12,3,46,45,68]
a1=tuple(filter(lambda a:a%2==0,b))
print(a1)
