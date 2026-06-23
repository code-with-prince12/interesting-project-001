
# Program II

class Account:
    # Initialize initial balance and private account number
    def __init__(self, balance, accountnumber):
        self.balance = balance
        self.__accountnumber = accountnumber  # Encapsulation Private attribute
    # Securely Access the Account Number
    def get__accountnumber(self):
        return self.__accountnumber
    # Deduct funds from the account balance
    def debit(self, amount):
        self.balance-=amount
        print("rs.", amount, "was debited")
    # Add funds to the account balance
    def credit(self, amount):
        self.balance+=amount
        print("rs.", amount, "was credited")
    # Format and display the current total balance
    def get_balance(self):
        total_balance = f"Total balance = {self.balance}"
        return total_balance
        
# Instantiate account object and run operations
account1 = Account(10000, 321)
account1.debit(500)
account1.credit(300)
print(account1.get_balance())
print(account1.get__accountnumber())

