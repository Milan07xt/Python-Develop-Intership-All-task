def a(func):
    def b():
        bb = func()
        return bb
    return b


def aa():
    return [x + 2 for x in a2]


a2 = [12, 3, 4, 6, 5, 61, 3, 13, 1, 31, 3, 13, 13]

a1 = a(aa)

print(a1())
