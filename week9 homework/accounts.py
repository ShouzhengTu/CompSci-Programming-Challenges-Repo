from pickle import NONE
import time
from instansiate_account import current_account,savings_Account
start = time.monotonic()

open_accounts = {

    "Reon Morita": {
        "Forename": "Reon", 
        "Surname": "Morita",
        "Password": "12345", 
        "Origin Date": start, 
        "Account Type": "Current", 
        "Balance": 100, 
        "Rate": 0.1,
        "History":["+10","-10","+12"]
        },

    "Kiran Warnholz": {
        "Forename": "Kiran", 
        "Surname": "Warnholz", 
        "Password": "12345", 
        "Origin Date": start, 
        "Account Type": "Savings", 
        "Balance": 1000, 
        "Rate": 0.5,
        "History":["+10","-10","+12"]
        },
        
    "Johan Boudry": {
        "Forename": "Johan", 
        "Surname": "Boudry", 
        "Password": "12345", 
        "Origin Date": start, 
        "Account Type": "Current", 
        "Balance": 100, 
        "Rate": 0.1,
        "History":["+10","-10","+12"]
        },
    "Jasheer Iqbal": {
        "Forename": "Jasheer", 
        "Surname": "Iqbal", 
        "Password": "12345", 
        "Origin Date": start, 
        "Account Type": "Current", 
        "Balance": 100, 
        "Rate": 0.1,
        "History":["+10","-10","+12"]
        },
    "Michelle Hoon": {
        "Forename": "Michelle", 
        "Surname": "Hoon", 
        "Password": "12345", 
        "Origin Date": start, 
        "Account Type": "Current", 
        "Balance": 100, 
        "Rate": 0.1,
        "History":["+10","-10","+12"]
        },
    "Shouzheng Tu": {
        "Forename": "Shouzheng", 
        "Surname": "Tu", 
        "Password": "1984@2009", 
        "Origin Date": start, 
        "Account Type": "Savings", 
        "Balance": 100000000000000000000, 
        "Rate": 0.10,
        "History":["+10","-10","+12"]
        },
    }

made = {}

def auth_initiate_accounts(name,inputPassword=None, internal=False):
    if name in made:
        return made[name],None
    try:
        forename,surname,password,origin_stamp,accountType,balance,interest,history = open_accounts[name].values()
    except KeyError:
        return None, "Oops...Your account does not exist please try again or create a new one"

    if not internal and inputPassword != password:
        return None,"Oops...incorrect password please try again"

    if accountType == "Current":
        account =  current_account(forename,surname,password,origin_stamp,accountType,balance,interest,history)
    else:
        account =  savings_Account(forename,surname,password,origin_stamp,accountType,balance,interest,history)
    
    made[name] = account 
    return account, None