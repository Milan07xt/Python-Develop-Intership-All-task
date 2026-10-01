#Exercise: 

#Create list comprehension which will print only even numbers from given range. 

num=[]
a1=list(range(1,12))
for i in a1:
    if  i % 2==0:
        num.append(i)
print(num)

#Even Number
a1=[i for i in a1  if i%2==0]
print(a1)

#Even Number
a2=[i for i in range(1,15) if i % 2==0]
print(a2)

#Odd Number
a2=[i for i in range(1,15) if i % 2!=0]
print(a2)
