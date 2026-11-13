import os



def alert(text):
    print(len(text)*"-")
    print(text)
    print(len(text)*"-")

def proceed():
    alert(f"Proceed?")
    input()
    os.system("clear")
    

def selection(page):
    import menu
    import profile_management
    try:
        choice = int(input())
    except ValueError:
        print("Oops...invalid value")
        proceed()
        if page == "Menu":
            menu.Main_menu_ui()
        else:
            profile_management.profile_management_menu_ui()
        return selection(page)
    return choice

def set_amount():
    try:
        alert("Please Enter The Amount")
        amount = int(input())
        return amount

    except ValueError:
        print("Oops...invalid value try again")
        proceed()
        return set_amount()
        