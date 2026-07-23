import json

with open('account.json', 'r') as file:
    account = json.load(file)

print('Welcome to ATM')
print()

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

def save_account():
    with open('account.json', 'w') as file:
        json.dump(account, file)

while True:
    print('1. Check balance')
    print('2. Deposit money')
    print('3. Withdraw money')
    print('4. Transaction history')
    print('5. Exit')
    print()
    while True:
        try:
            choice = int(input('Enter operation: '))
            if 1 <= choice <= 5:
                break
            else:
                print("Choose a number from 1 to 5.")
        except ValueError:
            print('Invalid value! Please enter a number.')
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
                save_account()
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
                save_account()
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
