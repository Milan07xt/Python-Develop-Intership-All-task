a=int(input("enter a age "))
if a==0  or a<0:
    print("You are not eligble")
elif 0<a<=30:
    print("free:100")
elif 30<a<=50:
    print("free:150")
elif 50<a<=70:
    print("free:200")
elif 70<a<=100:
    print("free:300")
else:
    print("free:500")
