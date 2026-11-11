

from instansiate_account import BankAccount
import transactions
import os

def open_accounts():
    accounts = {
        "Reon Morita":("Reon","Morita",100,"12345"),
        "Kiran Warnholz":("Kiran", "Warnholz",67000000,"12345"),
        "Johan Boudry":("Johan","Boudry",20,"12345"),
        }
    
    return accounts
    

def auth_initiate_accounts(name,inputPassword=None, internal=False):
    accounts = open_accounts()
    try:
        forename,surname,balance,password = accounts[name]
    except KeyError:
        return None, "Oops...Your account does not exist please try again or create a new one"

    if not internal and inputPassword != password:
        return None,"Oops...incorrect password please try again"
    
    return BankAccount(forename, surname, balance),None


def get_transfer_details(name):
    fore_recipients = input("Please enter forename:").strip().title()
    sur_recipient = input("Please enter surname:").strip().title()
    full_name  = fore_recipients+" "+sur_recipient
    recipient,error = auth_initiate_accounts(full_name,internal=True)
    if recipient is None:
        print(error)
        proceed()
        get_transfer_details(name)
    else: 
        amount = set_amount()
        transactions.transactions(name, recipient, amount)

def set_amount():
        try:
            amount = int(input("Please enter amount:"))
            return amount

        except ValueError:
            print("Oops...invalid value try again")
            proceed()
            set_amount()
        
def login_process():
    alert("Please enter forename:")
    forename = input().strip().title()
    alert("Please enter surname:")
    surname = input().strip().title()
    alert("Please Input Your Password")
    password = input()
    full_name  = forename+" "+surname
    name,error = auth_initiate_accounts(full_name,password)
    if name is None:
        print(error)
        proceed()
        login()
    else:
        menu_initialise(name)
    

def login_menu_ui():
    alert("📶Welcome to the Ultimate Banking Algorithm📶")
    alert("Please Login")

def login():
    login_menu_ui()
    login_process()

#Choice & value interchange
def choices_main(choice,name):
    if choice == 1:
        os.system("clear")
        initiate_withdraw(name)
    elif choice == 2:
        os.system("clear")
        initiate_deposit(name)
    elif choice == 3:
        os.system("clear")
        get_transfer_details(name)
    elif choice == 4:
        os.system("clear")
        profile_management(name)
    elif choice == 5:
        exit()

def initiate_withdraw(name):
    alert("Please Input Amount to Withdraw")
    amount = set_amount()
    name.auth_withdraw(amount)

def initiate_deposit(name):
    alert("Please Input Amount to Deposit")
    amount = set_amount()
    name.deposit(amount)

def Main_menu_ui():
    alert("📶Welcome to the Ultimate Banking Algorithm📶")
    texts = [
        "1. Withdraw",
        "2. Deposit",
        "3. Transfer",
        "4. Profile Management"
        ]
    for text in texts:
        print(text+"\n")
    alert("Please select the function you require")

def menu_initialise(name):
    while True:
        os.system("clear")
        Main_menu_ui()
        choice = selection()
        choices_main(choice,name)
        proceed()

def profile_management_menu_ui():
    alert("Profile Settings")
    texts = [
        "1. Update Forename",
        "2. Update Surname",
        "3. Profile Info",
        "4. View Transaction History",
        "5. Back to Main Menu"
        ]
    for text in texts:
        print(text+"\n")
    alert("Please select the function you require")


def profile_management(name):
    while True:
        os.system("clear")
        profile_management_menu_ui()
        choice = selection()
        choices_value_interchange_profile_management(choice,name)
        proceed()


def choices_value_interchange_profile_management(choice,name):
    if choice == 1:
        os.system("clear")
        name_update_fore(name)
    elif choice == 2:
        os.system("clear")
        name_update_sur(name)
    elif choice == 3:
        os.system("clear")
        name.get_profile()
    elif choice == 4:
        os.system("clear")
        print(name.get_transaction_history())
    elif choice == 5:
        os.system("clear")
        menu_initialise(name)

def name_update_fore(name):
    foreName = input("Please Enter Forename:")
    newName = name.set_forename(foreName)
    alert(f"Forename Changed to {newName}")


def name_update_sur(name):
    newSurname = input("Please Enter Surname:")
    newName = name.set_surname(newSurname)
    alert(f"Surname Changed to {newName}")


def stock_picker():
    pass

# UI & UX setup 
def alert(text):
    print(len(text)*"-")
    print(text)
    print(len(text)*"-")

def selection():
    choice = int(input())
    return choice

def proceed():
    alert(f"Proceed?")
    input()
    os.system("clear")

def main():
    os.system("clear")
    login()

main()