student_info={
    "name":"asfdvxz",
    "age":56,
    "marks":545
    }
print(student_info)

student_info.update({
    "name":"fsaxz",
    "age":46,
    "marks":465
})
print(student_info)



student_info["sagdvz"]={
    "name":"fssfxzaxz",
    "age":465,
    "marks":4655
}
print(student_info)


student_info.popitem()
print(student_info)

def count(n):
    cd={}
    for i in range(1,n+1):
        cd[i]=i**3
    return cd
print(count(5))

def count(a):
    count={}
    for char in a:
        count[char]=a.count(char)
    return count
print(count('sfavzx'))




student_info["sagdvz"]={
    "name":"fssfxzaxz",
    "age":465,
    "marks":4655
}
a=student_info.get("name")
print(a)

a=dict.fromkeys("name","sfavxz")
print(a)


def re_sum(n):
    if  n<=1:
        return n
    else:
        return n * re_sum(n-1)
print(re_sum(12))
