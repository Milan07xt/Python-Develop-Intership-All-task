def fac(n):
    if n <=1:
        return n
    else:
        return n* fac(n-1)
n=int(input("enter a number:"))
print(fac(n))
