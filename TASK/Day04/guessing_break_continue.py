import random
number=random.randint(1,200)
a=45
guess_number=False
guess=1
while not guess_number:
    if number == a:
        print("you are win")
        guess_number=True
        break
        number=int(input("guess again:"))
    else:
         if number < a:
            print("low")
            guess_number=False
            continue
            number=int(input("guess again:"))
         if number > a:
            print("low")
            guess_number=False
            number=int(input("guess again:"))
