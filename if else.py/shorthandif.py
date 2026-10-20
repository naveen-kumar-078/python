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