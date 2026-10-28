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
    




age = int(input("enter you age: "))
id = input("you id card yes/no: ")

if age>=18:
    if id == "yes":
        print("you re eligible")
    else:
        print("id required") 
else:
    print("no eleogibe")   



#atm withdrwal

pin = int(input('enter your pin: '))
balance= 5000

if pin == 1234:
    amount = int(input("enter your withdrwal amount: "))

    if amount > 0 :
        if  amount <= balance:
            balance = balance - amount
            print("withdrwal successfull")
            print("you balance amount",balance)
        else:
            print("insufficent balance")
    else:
        print("invalid amount")
else:
    print("wrong pin")

    


# student mark:

mark = int(input("enter your mark here: "))

if mark >= 35:
    attence = int(input(" enter you attence here: "))

    if attence >= 75:
        print("eligible to pass")
    else:
        print("attendence shortage")
else:
    print("fail")




# electricity bill

unit = int(input("enter your unit here :  "))

if unit <=0:
    print("invalid units")
else:
    if unit <=100:
        print("low usage")
    else:
        if unit >=300:
            print("high usage")
        else:
            print("medium usage")





