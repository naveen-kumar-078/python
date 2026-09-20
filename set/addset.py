thisset = {"apple", "banana", "cherry"}
thisset.add("pineapple")
print(thisset)


# to update the set  from one set to another :

theset  = {"cricket" , "ball", "bat"}
myset  = {"football", "ball", "kite"}

theset.update(myset)
print(theset)


#Add elements of a list to a set:
thisset = {"apple", "banana", "cherry"}
mylist  = ["watermelon"]
thisset.update(mylist)
print(thisset)