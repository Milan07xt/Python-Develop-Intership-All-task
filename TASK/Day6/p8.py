def great(a,b,c):
    if a> b and a>c:
        return a
    if b > a and b>c :
        return b
    else:
        return c
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=great(a,b,c)
print("greater than is:",d)
