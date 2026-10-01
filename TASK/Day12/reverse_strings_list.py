#String List Comprehenstion

a=["sac","advsz","vdxz"]
a1=[]
for i in a:
    a1.append(i[0])
print(a1)

a1=["sac","advsz","vdxz"]
a=[i[0] for i in a1]
print(a)



#Exercise: 

# define a function that take list of strings  

# list containing reverse of every string 

# NOTE - USE LIST COMPREHENSION because we already did this exercise  

# using normal method 

# example  

# l = ['abc', 'tuv', 'xyz'] 

# reverse_string(l) ----> ['bac', 'vut', 'zyx'] 

def li(a1):
    a=[]
    for i in a1:
        a.append(i[::-1])
    return a
print(li(["svzx","svxz","dvxz"]))


def reverse_strings(l):
    return [name[::-1] for name in l] 
print(reverse_strings(['abc', 'tuv', 'xyz'])) 

def reverse_str(l):
    new_list = []
    for name in l:
        new_list.append(name[::-1])
    return new_list 
print(reverse_str(['abc', 'tuv', 'xyz'])) 
