#List Comprehension

# with the help of list comprehension we can create of list in one line

#Positive List Comprehenstion
#First Method
a=[]
for i in range(1,12):
    a.append(i**2)
print(a)

#Second Method

s=[i**2 for i in range(1,11)]
print(s)

a=[]
for i in range(2,12):
    a.append(i**2)
print(a)
