def a(n):
    for i in range(1,n+1):
        yield(i)
for num in a(30):
    print(num)
 
