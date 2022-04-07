import os

def check_for_password():
    try:
        pwf = open("password.txt", "rt")
        pw = pwf.read()
        pwf.close()
    except FileNotFoundError:
        pw = input("No admin password found. Please set a password: ")
        pwf = open("password.txt", "wt")
        pwf.write(pw)
        pwf.close()
        
    return pw

def load_menus():
    menuf = open("menus.txt", "rt")
    menutext = menuf.read()
    menulist = menutext.split(";\n")
    return menulist

def file_menu():
    menu_loop = True
    while menu_loop:
        os.system('cls')
        print(load_menus()[0])
        ui = str(input("!> "))
        if ui == "1":
            return "new"
        elif ui == "2":
            return "open"
        else:
            input("Command not recognized. Press 'Enter' to try again.")
    return "error"
    
