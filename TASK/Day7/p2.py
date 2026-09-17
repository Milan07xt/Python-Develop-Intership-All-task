odd=0
even=0
i=1
while i <=5:
    number=int(input("Enter a Number:"))
    if number % 2 == 0:
                print("number is even ")
                even += number
    else:
        print("number is odd ")
    i+=1
print(even)
