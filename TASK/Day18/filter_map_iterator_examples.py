
numbers=[1,23,4,5,6,77,8,8,9,20]
squares = tuple(filter(map(lambda a:a**2,numbers))) # iterator  

print(squares) 

for i in squares:
    print(i) 
for j in squares:
    print(j) 
print(next(squares)) 
print(next(squares)) 
print(next(squares)) 
print(next(numbers)) #Error 

numbers = [1, 23, 4, 5, 6, 77, 8, 8, 9, 20]

squares = map(lambda a: a**2, numbers)

print(squares)

print(next(squares))
print(next(squares))
print(next(squares))

for i in squares:
    print(i)
