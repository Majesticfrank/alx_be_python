class BankAccount:
    def __init__(self, initial_balance):
       self. account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
   
    def withdraw(self, amount):
        if amount > self.account_balance:
             print("insufficient funds ")
         
        else:
             self.account_balance -= amount
             print(f"Withdrew ${amount}. Current balance is ${self.account_balance}")
   
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
if __name__ == "__main__":
    my_account =BankAccount(0)

