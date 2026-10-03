def find_pos(l, target):
    for pos, name in enumerate(l):
        if name == target:
            return pos
    return -1 
names = ['abc', 'abcdef', 'nityam'] 
print(find_pos(names,'nityam')) 

def a1(l, a):
    for pos, name in enumerate(l):
        if name == a:
            return pos
    return -1
names = ["zxv", "vxz", "svxz"]
print(a1(names, "vzx fcx"))

def a1(l,a):
    for pos,name in enumerate(l):
        if name == a:
            return pos
    return -1
names=["zxv","vxz","svxz"]
print(a1(names,"zxv"))

def a(a1,l):
    for b ,na in enumerate(a1):
        if na in l:
            return b
    return -1
name=["fdasvz","sfzvx","fzxv"]
print(a(name,"sfzvx"))

def a1(l,a):
    for aa,name in enumerate(a):
        if name in a:
            return aa
    return -1
names=["aaa","bbb","ccc"]
print(a1(names,"bbb"))
