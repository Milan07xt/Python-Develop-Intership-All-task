a=[]
for i in range(1,11):
    a.append(i**2)
print(a)

a=[i**2 for i in range(1,11)]
print(a)


a=[]
for i in range(1,11):
    a.append(-i**2)
print(a)

a=[-i**2 for i in range(-10,5)]
print(a)


a=[[1,2,3],[1,2,3],[1,2,3]]
for i in range(1,5):
    a.append(i)
print(a)
