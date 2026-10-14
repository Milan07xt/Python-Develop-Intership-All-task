def a(n):
    for i in range(1,n+1):
        yield i

for i in a(10):
    print(i)

