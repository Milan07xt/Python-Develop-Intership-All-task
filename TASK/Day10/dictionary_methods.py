a={
    "name":"unknown",
    "age":"unknown",
    "marks":"unknown"
  }
print(a)

a=dict.fromkeys(("name","age"),"unknown")
print(a)

a=dict.fromkeys("ads","unknown")
print(a)


a=dict.fromkeys(range(1,12),"unknown")
print(a)


a=dict.fromkeys("ads",["unknown","unknown"])
print(a)


b={"name":"dsa",
   "age":"unknown"}
print(b.get('name'))
c=b.get("name")
print(c)

d=b.get("age")
print(d)

if "name" in b:
    print("fsax")
else:
    print("fszXscx")

print(a.copy())


cc=a.clear()
print(c)

a1=a
print(a1 is a)
print(a1 == a)


