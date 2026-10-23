x = 11

if x > 10:
    print("X is above 10")

    if x > 20:
        print(" and also above 20")

    else:
        print("but not above 20")


#login system

username = input("Username: ")
password = input("Password: ")

if username == "admin":
    if password == "python123":
        print("Login successful")
    else:
        print("Password error")
else:
    print("Invalid username")
    
