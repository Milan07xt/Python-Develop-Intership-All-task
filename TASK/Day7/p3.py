def aa(a,b):
    if a > b:
        return a
    else:
        return b
def bb(a,b,c):
    cc= aa(a,b)
    return aa(cc,c)
print(bb(100,200,5500))
