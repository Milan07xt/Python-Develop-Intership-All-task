user_info={
    "name":"dsafzC",
    "age":24,
    "marks":56,
    }
print(user_info)

a={
    "name":"fsavxz",
   "age":20,
   "marks":65
   }

#First Method
user_info.update(a)
print(user_info)
#Second Method 
user_info.update({})
print(user_info)

