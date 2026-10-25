fruits=["orange","grapes","apple","mango"]
fruits.sort()
print(fruits)
print(sorted(fruits))

fruits1=["orange","grapes","apple","mango"]
fruits1.sort()
print(fruits1)
print(sorted(fruits1))

'''
fruits2 = ('grapes', 'mango', 'apple') 
fruits2.sort() 
print(fruits2)  # Error 
print(sorted(fruits2))   # Emmutable 
'''

guitars = [ 
{'model': 'yamaha f310', 'price':8400}, 
{'model': 'faith naptune', 'price':50000 }, 
{'model': 'faith apollo venus', 'price': 35000}, 
{'model': 'taylor 814ce', 'price': 450000} 
] 
print(sorted(guitars,key=lambda d:d["price"]))
print(guitars)
print(sorted(guitars,key=lambda d:d["model"]))
print(sorted(guitars,key=lambda d:d["price"],reverse=True))
