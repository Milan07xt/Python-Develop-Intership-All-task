class laptop:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self._price=price
    def p1(self):
        return f"{self.brand}  {self.model}  {self._price}"
p=laptop("HP","I5-7Gen",45000)
print(p.p1())

print(laptop.laptop_price)


# Encapsulation 
# Abstraction 
# Some special naming convention 
# Name Mangling , __name (not a convention) 
  
  
class Phone: 
    def __init__(self, brand,model_name, price): 
        self.brand = brand 
        self.model_name = model_name 
        self._price = price 
 # self.__price = price 
        self.complete_specification = f"{self.brand} {self.model_name} and price is {self._price}" 
      
    def make_a_call(self, phone_number): 
        print(f"calling {phone_number} ...") 
      
    def full_name(self): 
        return f"{self.brand} {self.model_name}" 
  
      
    def send_mesaage(self): 
        pass # twilio 
  
phone1 = Phone('nokia', '1100',1000)  
# print(phone1._price) 
 
# phone1._price = -1000 
# print(phone1._price) 
 
# print(phone1.__price)  #Error 
 
#print(phone1.__dict__) 
print(phone1._Phone__price) 
phone1._Phone__price = -1000 
print(phone1._Phone__price) 
  
  
  
  
  
# _name # convention of private name 
# __name__ # dunder/magic methods  
  
# l = [3,4,1,2] 
# l.sort() # tim sort , Timsort is a hybrid stable sorting algorithm, derived from merge sort and insertion sort,designed to perform well on many kinds of real-world data. 
# print(l) 
