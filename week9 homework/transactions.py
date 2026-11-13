import threading
from accounts import auth_initiate_accounts
from utilities import alert,proceed,set_amount


LOCK = threading.Lock()

def get_transfer_details(name):
    alert("Please enter forename")
    fore_recipients = input().strip().title()
    alert("Please enter surname:")
    sur_recipient = input().strip().title()
    full_name  = fore_recipients+" "+sur_recipient
    recipient,error = auth_initiate_accounts(full_name,internal=True)
    if recipient is None:
        print(error)
        proceed()
        get_transfer_details(name)
    else: 
        amount = set_amount()
        with LOCK:
            name.transactions(recipient, amount)

def initiate_withdraw(name):
    alert("Please Input Amount to Withdraw")
    amount = set_amount()
    with LOCK:
        name.auth_withdraw(amount)

def initiate_deposit(name):
    alert("Please Input Amount to Deposit")
    amount = set_amount()
    with LOCK:
        name.deposit(amount)

