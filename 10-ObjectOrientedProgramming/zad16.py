class BAccoumt():
    def __init__(self):
        self.bank_account_balance = 0
        

    def create_BA(self,num):
        self.Account_No = num

    def display_balance(self):
        print(f"Bank Account No:{self.Account_No}")
        print(f"Balance: PLN {self.bank_account_balance}")

    def add_balance(self,num):
        self.ammount = num
        self.bank_account_balance = self.bank_account_balance + self.ammount
        return  self.bank_account_balance

    def withdraw_balance(self,num):
        self.withdraw = num
        if  self.withdraw > self.bank_account_balance:
            print("Insufficient funds on the account")
        else:
            self.bank_account_balance = self.ammount - self.withdraw
        return  self.bank_account_balance

#12 3456 5555 9090 1111 0000 7722
b = BAccoumt()
b.create_BA("12 3456 5555 9090 1111 0000 7722")
b.add_balance(25.30)
b.display_balance()
b.withdraw_balance(31.70)
b.display_balance()
b.withdraw_balance(14)
b.display_balance()
