def a1(n, j="fscaxz",*args,**kwargs):
    print(n)
    print(j)
    print(args)
    print(kwargs)
a1("davz",1,2,3,4,a=12,b=23)

  
def func(name, *args, last_name = 'unknown', **kwargs): 
    print(name) 
    print(args) 
    print(last_name) 
    print(kwargs) 
  
func('Nityam', 1,2,3, a = 1, b = 2)

  
def func(l, **kwargs): 
    if kwargs.get('reverse_str') == True: 
        return [name[::-1].title() for name in l] 
    else: 
        return [name.title() for name in l] 
  
  
names = ['nityam', 'webtech'] 
print(func(names, reverse_str = True))


def a1(l, **kwargs):
    result = []

    if kwargs.get("reverse_str") == True:
        for name in l:
            result.append(name[::-1].title())
    else:
        for name in l:
            result.append(name.title())

    return result

name = ["sbxsg", "sgxvsfc"]

print(a1(name, reverse_str=True))
