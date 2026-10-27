#Short Hand If ... Else

a = 2
b = 320

print("A") if a > b else print("b")


a = 10
b = 20
bigger = a if a > b else b 
print("bigger",bigger)


a = 330
b  = 330

print ("a") if a > b else print("==") if (a==b) else print("b")




username = "bro"
displyname = username if username else ("guest")
print(displyname)


a = 10
b = 20

# Expected output: 20


print(b) if a < b else print(a) 



n = -5

# Expected output: Negative


print("negative") if n < 0 else print("postive")




n = 17

# Expected output: Odd


print("odd") if n%2==1 else print("even")






a = 15
b = 25
c = 10

# Expected output: 25


print(a) if a > b  else print(b) if b >c else print(c)



















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

