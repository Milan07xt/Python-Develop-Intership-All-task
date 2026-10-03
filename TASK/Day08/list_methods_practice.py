a=[1,2,3,4,5,6]
print(a)

a.append(10)
print(a)

a.extend("aa")
print(a)

a.remove(2)
print(a)

del a[2]

a=[1,3,2,4,5,6]
a.sort()
print(a)

a.clear()

a=["aa","bb","cc","sss"]
a.pop()
print(a)


a="dsffd"
a.title()
print(a)

a=[1,2,3,4,5]
a.reverse()
print(a)

a=[1,2,3,4,5,6]
b=[1,2,4,56,33]
c=[1,2,3,4,5,6]
aa = a is b
bb = a == c
print(aa)
print(bb)

a=[1,2,3,4,5,6]
a.clear()
print(a)

a=[1,2,3,4,5,6]
a.insert(1,77)
print(a)
