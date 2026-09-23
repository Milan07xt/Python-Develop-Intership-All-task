user_info={
    "name":"abc",
    "age" : 24,
    "marks":56,
    "afsvz":["vsa","vxz","vxzdavzx"]
    }
print(user_info)

if 'name' in user_info:
     print("aff")
else:
    print("fvzx")


if 24 in user_info.values():
     print("age number")
else:
    print("sfaxzgf")


if ["vsa","vxz","vxzdavzx"] in user_info.values():
    print("safdvszxc")
else:
    print("fzvxdv")


user_info_values=user_info.values()
print(user_info_values)

user_info_keys=user_info.keys()
print(user_info_keys)


user_items=user_info.items()
print(user_items)

for i in user_info:
    print(i)

for i in user_info.values():
    print(i)

for i in user_info.keys():
    print(i)

for i in user_info.items():
    print(i)

for i,j in user_info.items():
    print(f"key:{i},values:{j}")
