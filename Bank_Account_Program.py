class BankAccount:
    
    def __init__(self, new_name, checking_balance, savings_balance):
        self.name = new_name
        self.checking_balance = checking_balance
        self.savings_balance = savings_balance
        
    def deposit_checking(self, amount):
        amount = max(0,amount)
        self.checking_balance += amount
        
    def deposit_savings(self, amount):
        amount = max(0,amount)
        self.savings_balance += amount
        
    def withdraw_checking(self, amount):
        amount = max(0,amount)
        self.checking_balance -= amount
        
    def withdraw_savings(self, amount):
        amount = max(0,amount)
        self.savings_balance -= amount
        
    def transfer_to_savings(self, amount):
        amount = max(0,amount)
        self.checking_balance -= amount
        self.savings_balance += amount
