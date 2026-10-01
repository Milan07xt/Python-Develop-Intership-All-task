a=[[1,2,3] , [4,5,6],[7,8,9]]
print(a[1])

for i in a[1],a[2]:
    print(i)

a=a=[1,2,3,4,5,6,7,8,9]
print(a.index(2))

numbers =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,5,7,8,1] 
print(numbers.index(1)) 
print(numbers.index(1,3)) 
'''
#List inside List 
# list inside list 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 2d list 
# 3 items --> 3 list  
print(matrix[2]) 
for sublist in matrix: 
    print(sublist) 
for sublist in matrix:     
    for i in sublist: 
        print(i) 
        print(matrix[2][0]) 


s = "string"
print(type(s)) 
print(type(matrix))
'''
