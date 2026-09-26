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





set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
setc = set1.union(set2)


set8 = {"apple","orange","mango"}
se9 = {1,2,3}
set10 = {"jhon","elena"}

allset = set8.union(se9,set10)
print(allset)




aset = {1,2,3}
btuple = (4,5,6)
all = aset.union(btuple)
print(all)

print("----------intersection")


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
c = set1.intersection(set2)
print(c)

a = {0,1,"apple","orange"}
b = {True,False,"banna","pista"}
c = a.intersection(b)
print(c)

print("--------------------------setjoindiffrenece------------------")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set3)



print("-------------------symatic differnece---------------")

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


