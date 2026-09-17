def aa(a,b,c):
    if a > b and a >c:
        return a
    if b > a and b >c:
        return b
    else:
        return c
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
total= aa(a,b,c)
print(total)
