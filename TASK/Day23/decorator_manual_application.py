def a(l):
    def b(*args, **kwargs):
        print("fszxvzv")
        return l(*args, **kwargs)
    return b
def a1(a2, b2):
    return a2 + b2
a1 = a(a1)
print(a1(12, 25))


def a(l):
    def b(*args, **kwargs):
        print("fszxvzv")
        return l(*args, **kwargs)
    return b
@a
def a1(a2, b2):
    return a2 + b2
print(a1(12, 25))
