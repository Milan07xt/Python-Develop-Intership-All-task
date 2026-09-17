#scope
a=5
def aa():
    global a
    a=7
    return a
print(a)
print(aa())
