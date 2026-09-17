a=[1,2,3,4,5]
print(a)
b=["aa","bb","cc","dd"]
print(b)

b=["aa","bb","cc","dd"]
print(b[2])

b=["aa","bb","cc","dd"]
b.append("assa")
print(b)

b=["aa","bb","cc","dd"]
b.extend("cc")
print(b)

b=["aa","bb","cc","dd"]
b.remove("bb")
print(b)

b=["aa","bb","cc","dd"]
b.insert(1,"assa")
print(b)

b=["aa","bb","cc","dd"]
del b[1]

b=["aa","bb","cc","dd"]
b.pop()
print(b)

b=["aa","bb","cc","bb","dd"]
b.count("bb")
print(b)

b=["aa","bb","cc","dd"]
c=[1,3,2,4,5,6]
c.sort()
print(c)

b=["aa","bb","cc","dd"]
b.reverse()
print(b)

b=["aa","bb","cc","dd"]
b.clear()
print(b)

b=["aa","bb","cc","dd"]
c_copy=b.copy()
print(c_copy)

a=[1,2,3,4,5,6]
b=[1,2,3,4]
c=[1,2,3,4,5,6]
print(a==c)
print(a is b)



fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi'] 
# pop method 
fruits.pop(1) 
# del  
del fruits[1] 
# remove   
fruits.remove('apple') 
# append , extend , insert 
# pop, remove, del  
print(fruits) 

