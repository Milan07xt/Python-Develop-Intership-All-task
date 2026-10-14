def a(n):
    for i in range(1,n+1):
        if i%2==0:
            yield(i)
        else:
            print("invalid number")
for num in a(10):
    print(num)
