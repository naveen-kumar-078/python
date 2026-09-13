mytuple = "apple","orange","mango"
print(mytuple[0])

mytuple = "apple","orange","mango"
print(mytuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])


#This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])


#checking the exiting value

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
if "banana" in thistuple:
    print("yes its having in this fruits tuple")
else:
    print("not having")