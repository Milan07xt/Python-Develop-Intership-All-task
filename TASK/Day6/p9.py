def great(a,b,c,d):
    if a > b and a > c and a > d:
        return a
    if b > a and b > c and b > d:
        return b
    if c > a and c > b and c > d:
        return c
    else:
        return d
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
d=int(input("enter a number:"))
e=great(a,b,c,d)
print(e)
