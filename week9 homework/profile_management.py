import os
from utilities import alert

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
    alert("Please select the function you require:")

def name_update_fore(name):
    foreName = input("Please Enter Forename:")
    newName = name.set_forename(foreName)
    alert(f"Forename Changed to {newName}")


def name_update_sur(name):
    newSurname = input("Please Enter Surname:")
    newName = name.set_surname(newSurname)
    alert(f"Surname Changed to {newName}")