even=0
odd=0
for i in range(1,5):
    num=int(input("enter a number"))
    if num % 2==0:
                print("number is even")
                even += num
    else:
        print("number is odd")
print("sum of even:",even)

