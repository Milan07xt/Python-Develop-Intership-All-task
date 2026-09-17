def aa(a,b):
    if a > b:
        return a
    else:
        return b
def bb(a,b,c):
    ss=aa(a,b)
    return aa(ss,c)
print(bb(1000,5000,9000))
