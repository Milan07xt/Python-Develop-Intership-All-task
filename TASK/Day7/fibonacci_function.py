def aa(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b, b + a
aa(10)
