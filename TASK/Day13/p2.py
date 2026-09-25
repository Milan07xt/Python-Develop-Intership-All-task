# dictionary comprehension
a={i:i**2 for i in range(1,10)}
print(a)

a=[]
for i  in range(1,12):
    a.append({i:i**2})
print(a)
    
a=[]
for i in range(1,10):
    a.append(i)
    if i %2==0:
        print({i:"even"})
    else:
        print({i:"odd"})
print(a)



a="afascz"
for a1 in a:
    a2={a1:a.count(a)}
    print(a2)
