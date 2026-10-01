#Exercise: 
# num to string  
# define a function  
# example  
# input ----->  [True, False , [1,2,3], 1, 1.0, 3]  
# output ------> ['1', '1.0', '3'] 


def num_to_string(l): 
    return [str(i) for i in l if (type(i) == int or type(i) == float) ] 
print(num_to_string([True, False , [1,2,3], 1, 1.0, 3])) 

num=[]
def num_to_sring(l):
    for i in l:
        if type(i) == int or type(i)== float:
            return str(i)
print(num_to_string([True, False , [1,2,3],12,232,563,65,[1, 1.0, 3]])) 
