a=[[1,2,3],[4,5,6],[7,8,9]]
a1=[]
for i in range(3):
    a.append([22,11,34])
print(a)


a1=[[i for i  in range(1,5)] for j in range(3)]
print(a1)


nested_comp = [[i for i in range(1,4)] for j in range(3)  ] 
print(nested_comp) 
