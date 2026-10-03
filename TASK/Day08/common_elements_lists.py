def common_elements(a, b):
    c = []

    for i in a:
        if i in b:
            c.append(i)

    return c


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

print(common_elements(a, b))
