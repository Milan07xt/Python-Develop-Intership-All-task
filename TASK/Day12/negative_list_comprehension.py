#Negative List Comprehenstion

#First Method
a=[]
for i in range(-10,10):
    a.append(-i**2)
print(a)

#Second Method
a=[i**2 for i in range(-10,10)]
print(a)

a=[]
for i in range(-15,10):
    a.append(i**3)
print(a)

