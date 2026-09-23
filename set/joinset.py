# the  union and update will join both sets 

thisset = {"apple", "banana", "cherry"}
anset = {"beetroot","carrot","brinjal"}

set3 =thisset.union(anset)
print(set3)


thisset = {"apple", "banana", "cherry"}
anset = {"beetroot","carrot","brinjal"}

set3 =thisset.union(anset)
print(set3)
print("-------------------------------------------------------------------------")


# we can join multiple sets

et1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

alset = et1.union(set2,set3,set4)
print(alset)




#Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)