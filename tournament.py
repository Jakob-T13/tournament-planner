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