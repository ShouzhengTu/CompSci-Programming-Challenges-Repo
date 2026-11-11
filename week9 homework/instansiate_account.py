class BankAccount:

    def __init__(self,forename,surname,starting_balance=0):
        self._forename = forename
        self._surname = surname
        self._balance = starting_balance
        self._transactionHistory  = []

    def get_forename(self):
        return self._forename

    def set_forename(self,newname):
        self._forename = newname
        return self._forename

    def get_surname(self):
        return self._surname

    def set_surname(self,newname):
        self._surname = newname
        return self._surname
    
    def get_balance(self):
        return self._balance

    def _withdraw(self, amount):
        if self._balance >= amount:
            self._balance = round(self._balance - amount, 2)
            self.history(f"-{amount}")
        else:
            print("Insufficient funds")
        print("Account Balance:", self._balance)

    def auth_withdraw(self,amount):
        self._withdraw(amount)

    def deposit(self, amount):
        self._balance += amount
        self.history(f"+{amount}")
        print("Account Balance:", self._balance)

    def get_profile(self):
        self._print_profile()
    
    def _print_profile(self):
        print("----------------------")
        print(self._forename)
        print(self._surname)
        print(self._balance)
        print(self._transactionHistory)
        print("----------------------")

    def history(self,action):
        self._transactionHistory.append(action)

    def get_transaction_history(self):
        return self._transactionHistory









    








    
    

