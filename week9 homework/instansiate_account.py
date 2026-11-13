import accounts

class BankAccount:

    def __init__(self,forename,surname,password,origin_stamp,accountType,starting_balance=0,history=None):
        self._forename = forename
        self._surname = surname
        self._balance = starting_balance
        self._accountType = accountType
        self._transactionHistory  = history
        self._origin_stamp = origin_stamp
        self._next_interest_at = origin_stamp

    def get_forename(self):
        return self._forename

    def set_forename(self,newname):
        self._forename = newname
        self.save(self._forename+" "+self._surname)
        return self._forename

    def get_surname(self):
        return self._surname

    def set_surname(self,newname):
        self._surname = newname
        self.save(self._forename+" "+self._surname)
        return self._surname
    
    def get_balance(self):
        return self._balance

    def _withdraw(self,amount):
        if self._balance >= amount:
            self._balance = round(self._balance - amount, 2)
            self.history(f"-{amount}")
        else:
            print("Insufficient funds")
        print("Account Balance:", self._balance)
        self.save(self._forename+" "+self._surname)

    def auth_withdraw(self,amount):
        self._withdraw(amount)
        
    def deposit(self,amount):
        self._balance += amount
        self.history(f"+{amount}")
        print("Account Balance:", self._balance)
        self.save(self._forename+" "+self._surname)

    def transactions(self,recipient,amount):
        self._balance = round(self._balance-amount,2)
        recipient._balance = round(recipient._balance + amount,2)
        print(self.get_balance())
        self.history(f"-{amount}")
        recipient.history(f"+{amount}")
        self.save(self._forename+" "+self._surname)

    def get_profile(self):
        self._print_profile()
    
    def _print_profile(self):
        print("----------------------")
        print("Forename:",self._forename)
        print("Surname:",self._surname)
        print("Balance:",self._balance)
        print("Transaction Hisotry:",self._transactionHistory)
        print("Account Type:",self._accountType)
        print("----------------------")

    def history(self,action):
        self._transactionHistory.append(action)

    def get_transaction_history(self):
        return self._transactionHistory

    def calc_interest(self,now):
        while now >= self._next_interest_at:
            self._balance = round(self._balance*(1+self._interest),2)
            self._next_interest_at += 10
            self.save(self._forename+" "+self._surname)

    def save(self,name):
        accounts.open_accounts[name]["Forename"] = self._forename
        accounts.open_accounts[name]["Surname"] = self._surname
        accounts.open_accounts[name]["Balance"] = self._balance
        accounts.open_accounts[name]["History"] = self._transactionHistory

class savings_Account(BankAccount):

    def __init__(self, forename, surname, password, origin_stamp, accountType, starting_balance=0,interest_rate=0.04,history=None):
        super().__init__(forename, surname, password, origin_stamp, accountType, starting_balance,history)
        self._interest = interest_rate
    
    def withdraw_limits(self):
        pass


class current_account(BankAccount):

    def __init__(self, forename, surname, password, origin_stamp, accountType, starting_balance=0,interest_rate=0.015,history=None):
        super().__init__(forename, surname, password, origin_stamp, accountType, starting_balance,history)
        self._interest = interest_rate

    




  













    








    
    

