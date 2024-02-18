def check_password(password):
    with open('passwords.text', 'r') as file:
        common_passwrods = file.read().splitlines()

    for i, common_password in enumerate(common_passwrods, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return
        print(f'{password}: ✅ (Unique)')
        