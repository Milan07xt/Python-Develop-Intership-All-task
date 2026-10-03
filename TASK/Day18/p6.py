def a(*args):
    avg=[]
    for i in args:
        avg.append(sum(i)/len(i))
    return avg
print(a([1,2,3],[4,5,6],[7,8,9],[10,11]))


a1=lambda *args: [sum(i)/len(i) for i in zip(*args)]
print(a1([1,2,3],[4,5,6],[7,8,9],[10,11]))
