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




username = ""
displyname = username if username else ("guest")
print(displyname)