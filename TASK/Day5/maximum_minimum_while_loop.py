i = 1
mx = 0
b = 0
while i <= 5:
    num = int(input(f"Enter number {i}: "))

    if num > mx:
        mx = num
    if num < b:
        b = num
    i += 1
print("Maximum =", mx)
print("minimum=", b)

