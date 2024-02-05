import string
import secrets

def contains_upper(password):
    for char in password:
        if char.isupper():
            return True
        
    return False

def contains_symbols(password):
    for char in password:
        if char in string.punctuation:
            return True
        
    return False

def generate_password(length, symbols, upper):
    combination = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if upper:
        combination += string.ascii_uppercase
    
    combination_length = len(combination)
    new_password = ''

    for i in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

if __name__=='__main__':
    new_password = generate_password(6, True, True)
    print(new_password)