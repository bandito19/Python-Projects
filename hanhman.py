from random import choice

def game():
    word = choice(['hello', 'secret', 'guess'])

    username= input("What is your name? ")
    print(f"Welcome to hangman, {username}!")

    guessed = ''
    tries = 3

    while tries > 0:
        blanks = 0
        print("Word: ", end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else :
                print('-', end='')
                blanks +=1

        print()

        if blanks == 0:
            print("You got it.")
            break

        guess = input("Enter a letter: ")
        if guess in guessed:
            print(f"You already used {guess} try another letter.")
            continue

        guessed += guess

        if guess not in word:
            tries -= 1
            print(f"Sorry, that was wrong..({tries} tries remaining)")

        if tries == 0:
            print("No more tries remaining.. You lost!")
            break


if __name__=='__main__':
   game()