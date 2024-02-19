import itertools
import string
import time

def common_guess(word):
    with open('words.txt', 'r') as words:
        words_list =  words.read().splitlines()
    if word.lower() in words_list:
        return f'Common match {word} (#({words_list.index(word)+1}))'
    

def brute_force(word, length, digits=False, symbols=False):
    chars = string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation
    attemps = 0
    for guess in itertools.product(chars, repeat=length):
        attemps +=1
        guess = ''.join(guess)
        if guess == word:
            return f'{word} was cracked in {attemps:,} guesses.'
        

def main():
    print("Searching...")
    password = 'pass9'
    start_time = time.perf_counter()
    if common_match := common_guess(password):
        print(common_match)
    else:
        if cracked := brute_force(password, length=5, digits=True, symbols=False):
            print(cracked)
        else:
            print("There was no match.")
    
    end_time = time.perf_counter()
    print(round(end_time - start_time, 2), 's.')


if __name__=='__main__':
    main()