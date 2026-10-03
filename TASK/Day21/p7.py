  
@decorator_function # shortcut 
def func1(): 
    print('this is function 1 ') 
  
func1() 
  
@decorator_function 
def func2(): 
    print('this is function 2')
func2()
func1 = decorator_function(func1) 
func1() 
