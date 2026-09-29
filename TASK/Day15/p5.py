def a1(**kwargs):
    for i in kwargs.values():
        if i % 2==0:
            print(i)

a1(a=10, b=15, c=20, d=25, e=30)

def count(**a):
    return len(a)
print(count(name="Milan", age=20, city="Rajkot"))
