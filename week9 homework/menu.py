from utilities import alert,proceed
from accounts import auth_initiate_accounts

def login_menu_ui():
    alert("📶Welcome to the Ultimate Banking Algorithm📶")
    alert("Please Login")

def login_process():
    alert("Please enter forename:")
    forename = input().strip().title()
    alert("Please enter surname:")
    surname = input().strip().title()
    alert("Please Input Your Password")
    password = input()
    full_name  = forename+" "+surname
    account,error = auth_initiate_accounts(full_name,password)
    if account is None:
        print(error)
        proceed()
        return login_process()
    else:
        return account
        
def Main_menu_ui():
    alert("📶Welcome to the Ultimate Banking Algorithm📶")
    texts = [
        "1. Withdraw",
        "2. Deposit",
        "3. Transfer",
        "4. Profile Management",
        "5. Exit to Home"
        ]
    for text in texts:
        print(text+"\n")
    alert("Please select the function you require:")

