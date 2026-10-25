def a(*args):
    if all([type(arg)==int or type(arg)==float for arg in args]):
        total=0
        for i in args:
            total+=i
        return total
    else:
        return "wrong input"
print(a(1,2,3,45,"dsv",[1,2,3,4]))
