import random
import string
import sys

print("type 'login' to enter your details or 'close' to close the app.")
userInput = input("")
login = True

file = open("staff.txt")
staff = file.read().strip().split()


def login():
    login = False
    while not login:
        print("Your login details")
        if userInput == 'login':
            userName = input('username: ').lower()
            password = input('password: ').lower()

            if userName and password == "":
                print("try again")
            if userName and password in staff:
                print("login successful")
                login = True
            else:
                print("wrong, try again")
        if userInput == 'close':
            sys.exit()
    else:
        login
file.close()
login()

while login:

    
    def randomStringDigits(stringLength=10):
        """Generate a random string of letters and digits """
        digits = string.digits
        return ''.join(random.choice(digits)
        for i in range(stringLength))
        randomStringDigits(10)
    
    print("type 'create' for new bank account or 'check' to check bank account or 'logout' to close session or 'close'")
    userOption = input("").lower()
    if userOption == 'create':
        print("enter your details")

        user_name = input("Account Name: ")
        open_balance = input("Opening Balance: ")
        account_type = input("Account Type: ")
        account_email = input("Account Email: ")
        account_number = randomStringDigits(10)
        print("Account Number:" + account_number)
        with open('customer.txt', 'a') as f:
            f.write(f"{user_name} {open_balance} {account_type} {account_email} {account_number}\n\n\n")
        
    if userOption == 'check':
        print("enter your account number")
        file = open("customer.txt")
        customer = file.read().strip().split()
        account_number = input("Account Number: ")
        if account_number in customer:
            print(f"{user_name} {open_balance} {account_type} {account_email} {account_number}\n\n\n")

    if userOption == 'logout':
        login()
    if userOption == 'close':
        sys.exit()
           

