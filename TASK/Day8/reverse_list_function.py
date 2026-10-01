def rev(l):
    r = []

    for i in range(len(l)):
        a = l.pop()
        r.append(a)

    return r


n = [1, 2, 3, 4]

print(rev(n))]


reverse_list = [1,2,3,4,5,6,7,8,9]
def reverse_list(l): 
    r_list = [] 
    
    for i in range(len(l)): 
        popped_item = l.pop() 
        r_list.append(popped_item) 
    
    return r_list 

numbers = [1,2,3,4]  
print(reverse_list(numbers))
