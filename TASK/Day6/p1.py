even=0
odd=0
i=1
while i <=5:
    num=int(input("enter a number:"))
    if num % 2 == 0:
                 print("num is even")
                 even += num
    else:
        print("num is odd")
    i += 1
print("sum of even is :",even)

