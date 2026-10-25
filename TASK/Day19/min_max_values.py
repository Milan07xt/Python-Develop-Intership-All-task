a=[12,13,14,15]
print(min(a))
print(max(a))

b=["scaxZ","sda","aa"]
print(min(b))
print(max(b))

a = {
    "student1": {"age": 25},
    "student2": {"age": 45}
}

print(max(a, key=lambda item: a[item].get("age")))
print(min(a,key=lambda item:a[item].get("age")))

students2 = [     
{'name':'jay', 'score':90, 'age':24}, 
{'name':'mohit', 'score':70, 'age':19}, 
{'name':'rohit', 'score':60, 'age':25} ]
print(max(students2, key = lambda item:item.get('score'))) 
print(max(students2, key = lambda item:item.get('score'))['name']) 
print(max(students2, key = lambda item:item.get('age'))['name'])


students2 = [     
{'name':'jay', 'score':90, 'age':24}, 
{'name':'mohit', 'score':70, 'age':19}, 
{'name':'rohit', 'score':60, 'age':25} ]
print(max(students2, key = lambda item:item.get('name'))) 
print(max(students2, key = lambda item:item.get('score'))['name']) 
print(max(students2, key = lambda item:item.get('age'))['name'])
