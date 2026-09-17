name=input("enter a you name:")
a=" "
for i in range(len(name)):
    if name[i] not in a :
        print(f"{name[i]}",name.count(name[i]))
        
