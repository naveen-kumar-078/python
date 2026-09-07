#accsesing list var
var  =  ["apple","banna","mango"]
print(f"accsing list: {var[0:2]}")


#change list 
var  =  ["apple","banna","mango"]
var[1]="watermelom"

print(var)
#change range of list
avar=["apple","banna","cherry","mango","rasberry"]
avar[1:3]="watermelom","pistacho"

print(avar)




#add list in py

#end of the item 

nm = [1,2,3,4,5]
nm.append(6)
print(f"this is the add list {nm}")


#add a value with the specif index
nm = [1,2,3,4,5]
nm.insert(2,7)
print(f"this is the add list {nm}")

#remove

nm = [1,2,3,4,5]
nm.remove(2)
print(nm)


#using the index value
var  =  ["apple","banna","mango"]
var.pop(2)
print(var)