import instansiate_account 

def transactions(sender,recipient,amount):
    sender._balance = round(sender._balance-amount,2)
    recipient._balance = round(recipient._balance + amount,2)
    print(sender.get_balance())
    sender.history(f"-{amount}")
    recipient.history(f"-{amount}")
