a={}
for i in range(1,10):
    a1={i**2}
    print(a1)

# sets comprehension  
s = {k**2 for k in range(1,11)} 
print(s)

a=["dfavz","vazx","zdvs"]
for i in a:
    name={i[0]}
print(name)

a=["dfavz","vazx","zdvs"]
a1={i[0] for i in a}
print(a1)

names = ['Jiten', 'mohit', 'rohit'] 
first = {name[0] for name in names} 
print(first) 
