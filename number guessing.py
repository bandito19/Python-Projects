from random import randint

lower, upper = 1, 10
random_number = randint(lower, upper)

print("Guess a number in the range from {lower} to {upper}")

while True:
    try:
        user_input  = int(input("Guess: "))
    except ValueError as e:
        print("please enter a valid number.")
        continue

    if user_input > random_number:
        print("Try a smaller number.")
    elif user_input < random_number:
        print("Try a bigger number.")
    else:
        print("You guessd it.")
        break