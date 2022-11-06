
class Person:
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

class Costumer(Person):
    def __init__(self, first_name, last_name, account_number, balance):
        super().__init__(first_name, last_name)
        self.account_number=account_number
        self.balance=balance

    def __repr__(self):
        datas=(self.first_name+" "+self.last_name+" Account number:"+str(self.account_number)+" Balance:"+str(self.balance))
        print (datas)
        return datas

    def deposit(self):
        addition=input("How much money do you want to add to your account? ")
        self.balance=int(self.balance)+int(addition)
        return self.balance

    def withdraw(self):
        withdrawal=input("How much money do you want to withdraw from your account? ")
        if int(withdrawal) > int(self.balance):
            print("There is not enough money in your account")
        else:
            self.balance=int(self.balance)-int(withdrawal)
            return self.balance


def code_execution():
    user.__repr__()
    while True:
        choice=input("""
Type the operation you want to execute:
    deposit - You can add money to your account
    withdraw - You can withdraw money from your account
    exit - Exit program
        """)
        if choice == "deposit":
            user.deposit()
            user.__repr__()
        elif choice == "withdraw":
            user.withdraw()
            user.__repr__()
        elif choice == "exit":
            print("Thank you for choosing the Gizmo National Bank!")
            break
        else:
            print("Unknown operation")


print("""
Welcome to the Gizmo National Bank.
Please provide the necessary information below.""")
user=Costumer(input("First name: "), input("Last name: "), input("Account number: "), input("Your current balance: "))
code_execution()











