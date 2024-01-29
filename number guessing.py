from random import randint

lower, upper = 1, 10
random_number = randint(lower, upper)

tries = 3
print(f"Guess a number in the range from {lower} to {upper}, You have {tries} tries")

while True:
    if tries > 0:
        try:
            user_input  = int(input("Guess: "))
            tries -= 1
        except ValueError as e:
            print("please enter a valid number.")
            continue
    else:
        print("You ran out of tries")
        break

    if user_input > random_number:
        print("Try a smaller number.")
    elif user_input < random_number:
        print("Try a bigger number.")
    else:
        print("You guessd it.")
        break