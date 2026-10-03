def a(l):
    odd = []
    even = []
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    aaa = [odd, even]
    return aaa

num=[1,2,3,4,5,6]
print(a(num))

    
