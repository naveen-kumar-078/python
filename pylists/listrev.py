#accsesing list var
var  =  ["apple","banna","mango"]
print(f"accsing list: {var[0:2]}")
#

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






#lists practise

fruits = ["apple", "banana", "mango", "orange"]
print(fruits[0])
print(fruits[2])
print(fruits[3])

colors = ["red", "blue", "green", "yellow"]
colors[1]="black"
colors[-1]="white"
print(colors)


movies = ["Leo", "Jailer", "Vikram"]
movies.append("master")
print(movies)



students = ["Arun", "Ravi", "Kumar"]
students.insert(1,"Naveen")
print(students)


a = ["Python", "Java"]
b = ["HTML", "CSS"]

a.extend(b)
print(a)


animals = ["dog", "cat", "lion", "tiger"]
animals.remove("lion")
print(animals)



numbers = [10, 20, 30, 40, 50]
numbers.pop(3)
print(numbers)




num = [10, 20, 30, 40, 50]
num[1]=25
num.append(60)
num.remove(40)
num.insert(0,15)
print(num)



food = ["pizza", "burger", "pasta"]
food.append("biriyani")
food.insert(1,"dosa")
food.remove("burger")
print(food)




laptop = ["Dell", "8GB RAM", "512GB SSD", "Windows"]
laptop[1]="16GB RAM"
laptop.append("i5 processor")
laptop[3]="linux"

print(laptop)