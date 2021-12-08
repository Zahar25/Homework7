import json
from datetime import datetime

class WithdrawException(Exception):
    pass
class LoginException(Exception):
    pass


def login (username, password):
        with open('users.json', 'r') as user_info:
            data = json.load(user_info)
        for user in data["users"]:
            if user["name"] == username and user["password"] == password:
                return username
        raise LoginException ("Invalid username or password. Try again")



def get_balance(username):
        with open(f'{username}_balance.json', "r") as user_balance:
            balance_data = json.load(user_balance)
            return balance_data



def money_withdraw (username, amount):
        amount = abs(amount)
        user_balance = get_balance(username)
        if user_balance >= amount:
            user_balance -= amount
        else:
            raise WithdrawException ("Invalid operation. Nedostatnio koshtiv. Try again")
            return

        
        set_balance(username, user_balance)
        add_transaction(username, -amount)


def money_put(username, amount):
    amount = abs(amount)
    user_balance = get_balance(username)
    user_balance += amount


    set_balance(username, user_balance)
    add_transaction(username, amount) 



def set_balance(username, balance):
        with open(f'{username}_balance.json', "w") as user_balance:
            balance_data = json.dump(balance,user_balance)
            return balance_data



def add_transaction(username, amount):
        transaction = {'data':str(datetime.now()), "amount": amount}
        with open (f'{username}_transactions.json', 'a') as user_transaction:
            user_transaction.write(json.dumps(transaction)+ '\n')

def start():
    while True:
            try:
                username = login(input("Enter name: "), input("Enter password: "))
            except LoginException:
                print("Invalid username or password. Try again")
            else:
                break
    while True:
            
        
        menu = input("Enter operation: \n1.My balance \n2.Withdraw money \n3.Put money \n4.Exit\n ")
        if menu == "1":
            print(f"Your balance: {get_balance(username)}")
        elif menu == "2":
            withdraw = int(input("How much do you want to withdraw ?: \n"))
            money_withdraw(username, withdraw)
        elif menu == "3":
            put = int(input("How much do you want to put ?: \n"))
            money_put(username, put)
        elif menu == "4":
             break
start()