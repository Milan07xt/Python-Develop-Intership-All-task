a=[1,2,3,4,5]
b=[6,7,8,9,10]
for i in a:
    avg=[]
    avg.append(i%2==0)
print(avg)
for i in b:
    avg1=[]
    avg1.append(i%2==0)
print(avg1)

for i in b:
    avg1=[]
    avg1.append(i%2==0)
print(all(avg1))
print(any(avg1))


print(all(avg))
print(any(avg))

print(any([i%2==0 for i in a]))
print(all([i%2==0 for i in a]))
