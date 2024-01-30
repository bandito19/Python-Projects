import random

def roll_dice(amount):
    if amount <=0:
        raise ValueError
    rolls = []
    for i in range(amount):
        random_roll = random.randint(1, 10)
        rolls.append(random_roll)
    
    return rolls


def main():
    while True:
        try:
            user_input = input("How many dice would you like to roll? : ")
            if user_input.lower() == 'exit':
                break
            rolls = roll_dice(int(user_input))
            print(*rolls, sep=', ')
        except ValueError:
            print("Please enter a valid number.")
        s = 0
        for i in range(len(rolls)):
            s += rolls[i]
        print("Sum of your rolls:", s)

        
if __name__=="__main__":
    main()
            
