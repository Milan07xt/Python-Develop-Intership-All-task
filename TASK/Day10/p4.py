User_info ={
    "name:":"avsx",
    "age":54,
    "marks":561,
    "Fav_movies":["gdsav","gvdxz","gdvzxc"]
    }
print(User_info)

User_info['fav_song']=["fadxvz","fsavzx","fsavxz"]
print(User_info)



pop_items=User_info["Fav_movies"]
print(pop_items)

poped_items=User_info.pop("age")
print(User_info)
print(poped_items)


poped_items=User_info.popitem()
print(poped_items)
