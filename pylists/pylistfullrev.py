fruits = ["apple","orangfe","mago"]
print(fruits)


my_details = ["naveen",21,"rathinam","bca"]
print(my_details)



# accessing items

fruits = ["Apple", "Banana", "Orange", "Mango"]
print(fruits[0])
print(fruits[1])


# negative  indexing 

its = ["Apple", "Banana", "Orange", "Mango"]
print(its[-1])



numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])

if 60  in numbers:
     print("yes it is")




#changing the list



fruits = ["Apple", "Banana", "Orange"]
fruits[2]  = "grapes"
print(fruits)

fruits = ["Apple", "Banana", "Orange"]

fruits[1:2] = ["mango","grapes"]
print(fruits)


#practise 
number = [10,20,30,40,50]
number[1]=100
number[3]=200
print(number)
number [1:3] = [300,400]
print(number)






#lists practise test

students = ["Arun", "Ravi", "Kumar", "Vijay"]
print(students[1])
print(students[-1])
print(students[1:4])
print("----------------------------------")




marks = [45, 60, 70, 80, 90]
marks[1] = 65
marks[4]  = 100
print(marks)



languages = ["Python", "Java", "C++"]
languages.append("javascript")
languages.insert(1,"HTML")
languages.append("css")
languages.append("sql")
print(languages)
