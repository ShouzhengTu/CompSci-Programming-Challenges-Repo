
import time 
import os
import threading
from accounts import auth_initiate_accounts, open_accounts
from utilities import proceed,selection
from menu import Main_menu_ui,login_process,login_menu_ui
from transactions import get_transfer_details,initiate_deposit,initiate_withdraw,LOCK
from profile_management import profile_management_menu_ui,name_update_fore,name_update_sur

def run_clock():
    while True:
        time.sleep(10)
        now = time.monotonic()
        with LOCK:
            for record in open_accounts:
                account,error = auth_initiate_accounts(record,internal=True)
                account.calc_interest(now)

                   

clock = threading.Thread(target=run_clock, daemon=True)
clock.start()

def login():
    login_menu_ui()
    name = login_process()
    menu_initialise(name)

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
        main()
        
def menu_initialise(name):
    while True:
        os.system("clear")
        Main_menu_ui()
        choice = selection("Menu")
        choices_main(choice,name)
        proceed()

def profile_management(name):
    while True:
        os.system("clear")
        profile_management_menu_ui()
        choice = selection("Pmenu")
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

def main():
    os.system("clear")
    login()

main()