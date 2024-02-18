def check_password(password):
    with open('passwords.txt', 'r') as file:
        common_passwrods = file.read().splitlines()

        if password in common_passwrods:
            print(f'{password}: ❌ (#{common_passwrods.index(password)+1})')
            return
        
    print(f'{password}: ✅ (Unique)')


def main():
    user_password = input('Enter a password: ')
    check_password(user_password)

if __name__ == '__main__':
    main()