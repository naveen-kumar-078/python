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
    
    
    if password!="python123":
        print("password eror")



#bank

balance = 5000
correctpin = 1234

pin = int(input("enter your pin here :"))

if pin == correctpin:
    amount = int(input("enter your withdrwal amount here "))


    if amount > 0:
        if amount<= balance:
            balance = balance-amount
            print("withdrwal amount",amount)
            print("remaining balance",balance)
        else:
            print("insufficent balance")
    else:
        print("insufficient amount")

else:
    print("incorrect pin")
    
    