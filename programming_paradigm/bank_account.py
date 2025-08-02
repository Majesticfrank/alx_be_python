class BankAccount:
    def __init__(self, initial_balance):
       self. account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance += amount
           
    def withdraw(self, amount):
        if amount > self.account_balance:
          return False
         
        else:
             self.account_balance -= amount
             return True
   
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

if __name__ == "__main__":
    my_account =BankAccount(0)
    my_account.deposit(67)
    my_account.deposit(200)
