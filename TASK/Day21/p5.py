def a(b):
    def c():
        print('This is an awesome function')
        b()
    return c

def d():
    print('This is function 1')
d = a(d)
d()

def a(ll):
    def b():
        print("gadvzx ")
        ll()
    return b
def d():
    print("gdszxc")
d=a(d)
d()
