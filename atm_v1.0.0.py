print('Welcome to ATM')
print()

account = {
    "name": "Bohdan",
    "balance": 1000,
    "pin": '1234'
}

password = ''
attempts = 3
history = []

while password != account['pin']:
    password = input('Enter your password: ')
    if password == account['pin']:
        print('Access granted!')
    else:
        attempts -= 1
        print('Wrong password! Try again!')
        print('Attempts', attempts,'of 3')
        if attempts == 0:
            print('Too many failed attempts!')
            print('Account blocked!')
            break
    print()
    
def show_balance():
    print('Current balance:',account['balance'])

while True:
    print('1. Check balance')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Transaction history')
    print('5. Exit')
    print()
    choice = int(input('Enter operation: '))
    if choice == 1:
        show_balance()
        print()
    elif choice == 2:
        while True:
            amount = int(input('Deposit money: '))
            if amount <= 0:
                print('Operation failed! Wrong amount!')
            else:
                account['balance'] += amount
                print('Deposit confirmed')
                show_balance()
                history.append(f"Deposit: +{amount}")
                print()
                break
    elif choice == 3:
        while True:
            amount = int(input('Enter sum to withdraw: '))
            if amount > account['balance']:
                print('Operation failed! Not enough money on your account!')
            elif amount <= 0:
                print('Operation failed! Wrong amount!')
            else:
                account['balance'] -= amount
                print('Withdraw confirmed')
                show_balance()
                history.append(f'Withdraw: -{amount}')
                print()
                break
    elif choice == 4:
        if len(history) == 0:
            print('No transactions yet!')
        else:
            for operation in history:
                print(operation)
        print()
    elif choice == 5:
        print('Thank you for using our ATM!')
        break
    else:
        print('Wrong choice!')
