n= int(input("enter a number"))
num=int(input("Enter a number [1]: "))
a =num#maximum
b = num#minimum
for i in range(2,n+1):
    num=int(input(f"Enter a number{i}: "))
    if a < num:
        a = num
    if b > num:
        b = num
print(a)
print(b)
