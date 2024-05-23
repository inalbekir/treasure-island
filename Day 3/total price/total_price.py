height = int(input("What's your height? "))

if height > 120:
    print("You can ride!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age < 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        bill = 0
        print(f"Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    wants_photo = input('Do you want photo? Y or N. ')
    if wants_photo == 'Y':
        bill += 3
        print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller.")