def a(**kwargs):
    for k,v in kwargs.items():
        print(f"{k}:{v}")
d={"name":"sgvdz","age":4}

a(**d)
