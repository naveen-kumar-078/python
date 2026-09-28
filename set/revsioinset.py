language  = {"Python", "Java", "C++", "JavaScript"}
print(language)


#check an item
fruits = {"apple", "banana", "mango"}
print( "banana" in fruits)



#add an item

colors = {"red", "blue", "green"}
colors.add("yellow")
print(colors)

numbers = {10, 20, 30}
num2  = {40,50,60}

numbers.update(num2)
print(numbers)



#to remove an set
fruits = {"apple", "banana", "mango", "orange"}
fruits.remove("mango")
print(fruits)


#join two set

a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)


#find common items

a = {"apple", "banana", "cherry"}
b = {"banana", "cherry", "orange"}

c = a.intersection(b)
print(c)


#find difference

a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

c = a.difference(b)
print(c)


#update using dffernce

a = {"apple", "banana", "cherry"}
b = {"apple", "orange"}
a.difference_update(b)
print(a)


a = {1, 2,5}
b = {1, 2, 3, 4}

print(a.issubset(b))