def a(aa):
    return aa*2
n=[1,2,3,4,5,6,7]
a1=list(filter(a,n))
print(a1)

def a(aa):
    return aa%2==0
n=[1,2,3,4,5,6,7]
a1=tuple(filter(a,n))
print(a1)

def is_even(a):
    return a%2 == 0 
numbers = [3,4,2,1,5,6,9,8,10] 
evens = tuple(filter(is_even, numbers) )
print(evens)


evens = tuple(filter(lambda a:a%2==0, numbers)) 
print(evens) 
evens = filter(lambda a:a%2==0, numbers) 
for i in evens:
    print(i) 
'''new_evens = [i for i in numbers if i%2==0] 
print(evens) 
print(list(evens)) 
print(new_evens)
'''
b = [3,4,2,1,5,6,9,8,10]
a1=tuple(filter(lambda a: a%2==0,b))
for i in a1:
    print(a1)


b=[1,2,3,4,66,56,7,7,88,99]
print(tuple(filter(lambda a:a%2==0,b)))

b=[1,2,3,4,66,56,7,7,88,99]
print(tuple(filter(lambda a:a%2==0,b)))
