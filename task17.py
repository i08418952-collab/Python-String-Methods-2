password = input('password: ')
if any(b.isdigit() for b in password):
    print(True)
else:
    print(False)    