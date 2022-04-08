import os

def load_menus():
    menuf = open("menus.txt", "rt")
    menutext = menuf.read()
    menulist = menutext.split(";\n")
    return menulist

def file_menu():
    while True:
        os.system('cls')
        print(load_menus()[0])
        ui = str(input("!> "))
        if ui == "1":
            return "new"
        elif ui == "2":
            return "open"
        else:
            input("Command not recognized. Press 'Enter' to try again.")
    return None
    
def open_tourn(mode):
    if mode == "new":
        invalid_input = True
        dict_size = 0
        while invalid_input:
            ui = int(input("Enter desired number of participants: "))
            if ui < 1:
                print("You must have at least 1 participant.")
            else:
                dict_size = ui
                invalid_input = False
        working_dict = {}
        for i in range(dict_size):
            working_dict[i+1] = None
        return working_dict
    elif mode == "open":
        invalid_input = True
        working_dict = {}
        while invalid_input:
            fname = input("Enter the full file name of the file you want to open: ")
            try:
                csv = open(fname, "rt")
                csv_txt = csv.readlines()
                csv.close()
                csv_txt.pop(0)
                for i in range(len(csv_txt)):
                    csv_txt[i].split(",")
                    csv_txt[i][0] = int(csv_txt[i][0])
                    working_dict[csv_txt[i][0]] = csv_txt[i][1]
                print("Successfully loaded " + fname)
                return working_dict
            except:
                input("Failed to find file. Press 'Enter' to continue...")
                return None
    else:
        print("An error has occurred.")
        return None
    return None
    
def entry_menu(tdict):
    working_dict = tdict
    tsize = len(tdict)
    slot_prompt = f"Enter desired starting slot (1-%d), or type '0' for first available: % {tsize}"
    while True:
        os.system('cls')
        print(load_menus()[1])
        ui = str(input("#> "))
        if ui == "1":
            invalid_name = True
            while invalid_name:
                ui = str(input("Enter name: "))
                if ui in working_dict.values():
                    input("That name is already in the tournament. Press 'Enter' to try again.")
                else:
                    newname = ui
                    invalid_name = False
            invalid_place = True
            while invalid_place:
                uin = int(input(slot_prompt))
                if uin == 0:
                    cur_val = working_dict[1]
                    i = 1
                    while cur_val != None:
                        i++
                        cur_val = working_dict[i]
                    working_dict[i] = newname
                    invalid_place = False
                elif uin > tsize or uin < 1:
                    input("That number is outside the required range. Press 'Enter' to try again.")
                else:
                    if working_dict[uin] == None:
                        working_dict[uin] = newname
                        invalid_place = False
                    else:
                        input("That slot is already taken. Press 'Enter' to try again.")
            input("Success! The new entrant has been added. Press 'Enter to continue.")
        elif ui == "2":
            uin = int(input(f"Starting slot (1-%d): % {tsize}"))
            ui = input("Participant name: ")
            if working_dict[uin] == ui:
                working_dict[uin] = None
                print(f"Success:\n%s has been removed from slot %d. % {ui, uin}")
            else:
                print(f"Failure: %s is not in slot %d. % {ui, uin}")
            input("Press Enter to continue.")
        elif ui == "3":
            uin = int(input(f"Choose a slot (1-%d):  % {tsize}"))
            if uin < 1 or uin > tsize:
                print("Error: invalid slot.")
            else:
                for n in range(-5,0):
                    try:
                        print(f"%d: %s % {uin+n, working_dict[uin+n]}")
                    except:
                        print("")
                print(f"%d: %s % {uin, working_dict[uin]}")
                for n in range(1,6):
                    try:
                        print(f"%d: %s % {uin+n, working_dict[uin+n]}")
                    except:
                        print("")
            input("Press Enter to continue.")
        elif ui == "4":
            return working_dict
        else:
            input("Command not recognized. Press 'Enter' to try again.")
    return None
    
def admin_menu(tdict):
    working_dict = tdict
    while True:
        os.system('cls')
        print(load_menus()[2])
        ui = str(input("@> "))
        if ui == "1":
            savename = input("Enter file name to save to (no extension): ")
            savename = savename + ".csv"
            print(f"Generating csv and saving to %s... % {savename}")
            dictkeys = working_dict.keys()
            dictvals = working_dict.values()
            csv_txt = '"slot","name"\n'
            for i in range(len(dictkeys)):
                csv_txt += f'%d,"%s"\n % {dictkeys[i], dictvals[i]}'
            savef = open(savename, "wt")
            savef.write(csv_txt)
            savef.close()
            input("Save successful. Press Enter to continue...")
        elif ui == "2":
            return "entry"
        elif ui == "3":
            return "exit"
        else:
            input("Command not recognized. Press 'Enter' to try again.")
    return None

def main():
    