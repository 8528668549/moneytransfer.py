class BankAccount:
    def __init__(self,account_number):
        self.account_number = str(account_number)
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("insufficient funds")

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

def transfer_amount(acc_1, acc_2, amount):
    acc_1.withdraw(amount)
    acc_2.deposit(amount)

user_1 = BankAccount("001")
user_2 = BankAccount("002")
user_1.deposit(400)
user_2.deposit(200)

print("user 1 Balance: {}/-".format(user_1.get_balance()))
print("user 2 Balance: {}-".format(user_2.get_balance()))

transfer_amount(user_1, user_2,100)
print("")

print("transferring 50/-".format(user_1.get_balance()))
print("user 1 balance: {}/-".format(user_1.get_balance()))
print("user 2 balance: {}/-".format(user_2.get_balance()))
