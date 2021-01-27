print('Welcome to IHS towers')
answer = input("Are you an IHS staff? yes/no")

if answer == 'yes':
    password = int(input('Please enter your password?'))
    if password == 2021:
        print('Access granted!')
    else:
        print('Wrong password')
else:
    print('Access denied!')



