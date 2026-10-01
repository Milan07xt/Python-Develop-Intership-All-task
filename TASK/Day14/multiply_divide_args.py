# *args with normal parameter 
 
def multiply_nums(*args): 
    multiply = 1 
    
    for i in args: 
        multiply *= i 
    return multiply 
  
print(multiply_nums(2,4,3,4))


def divide1(*args):
    divide=1
    for i in args:
        divide /=i
    return divide
print(divide1(2,4,6,8))
    
