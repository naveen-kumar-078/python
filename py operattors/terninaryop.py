a = int(input())
result = "even"if a%2==0 else "odd"
print(result)


b = input("enter your number")

re = "POSTIVIE" if a>0 else "negative"
print(re)


a = int(input())
b = int(input())
c = int(input())

result = a if a > b and a > c else  ( b  if b> a and b>c else c)
print(result) 




username = input("enter your username")
password = input("enrter your password")

result = "login successfully" if username =="admin" and password =="123456" else "invalid username and passswokrd"
print(result)